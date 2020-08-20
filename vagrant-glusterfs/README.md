# GlusterFS Server and Heketi Server on Vagrant

이 Vagrant와 Ansible 코드는 다음 4개의 가상 서버에 [GlusterFS](https://www.gluster.org/)와 [Heketi](https://github.com/heketi/heketi)를 구축하여, 쿠버네티스 클러스터의 파드에서 마운트하여 사용할 수 있게 해준다. 이 가상 서버의 IP 주소는 가성 서버에 할당된 내부 통신용 IP 주소다. 

1. heketi   172.20.1.20  
1. gluster1 172.20.1.21　
1. gluster1 172.20.1.22
1. gluster1 172.20.1.23

vagrant-kubernetes로 구축하는 쿠버네티스 클러스터와 조합하여, 퍼시스턴트 볼륨을 자동 프로비져닝을 환경을 위한 것이다. 

## 이 클러스터를 기동하기 위해 필요한 소프트웨어 

다음 소프트웨어를 설치해야 한다. 

* Vagrant (https://www.vagrantup.com/)
* VirtualBox (https://www.virtualbox.org/)
* kubectl (https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* git (https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## 가상 머신의 호스트 환경

Vagrant와 VirtualBox가 동작 중인 OS가 필요

* Windows10　
* MacOS
* Linux

저자의 테스트 환경은 다음과 같다. 

* RAM: 8GB 
* 남은 저장 공간: 5GB 
* CPU: Intel Core i5

## GlusterFS와 Heketi 서버 기동

다음의 명령어로 GlusterFS와 Heketi를 위한 노드가 기동한다.

```
$ git clone https://github.com/takara9/vagrant-glusterfs
$ cd vagrant-glusterfs
$ vagrant up
```

## 쿠버네티스 파드에서 이용

vagrant-kubernetes로 구축한 클러스터로 테스트하기 위해서는 k8s-yaml 매니페스트를 적용한다. 

쿠버네티스 클러스터의 마스터 노드에 로그인하여, 레포지터리를 복사하고 다음 디렉터리로 이동한다. 

```
$ vagrant ssh master
$ git clone https://github.com/takara9/vagrant-glusterfs
$ cd vagrant-glusterfs/k8s-yaml
```

이 디렉터리에는 Heketi와 연동할 프로비저너를 정의한 스토리지가 있다. 
그리고 슽뢰지를 다이나믹 프로비저닝하는 샘플 매니페스트가 있다. 
GlusterFS를 마운트하는 파드를 기동하여 확인할 수 있다. 

```
kubectl apply -f storageclass.yml (스토리지 클래스에 Heketi의 엔드포인트 등록)
kubectl apply -f gfs-pvc-1.yml (Persistent Volume Claim으로 PV 프로비저닝)
kubectl apply -f gfs-client.yml (PVC를 마운트하는 파드를 2개 기동)
```

PVC와 PV의 생성을 확인하는 방법은 다음과 같다.(Windows10의 경우)

```
C:\Users\Maho\vagrant-glusterfs\k8s-yaml>kubectl get pvc
NAME      STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS     AGE
gvol-1    Bound     pvc-d8538128-2a07-11e9-b4c1-02f6928eb0b4   10Gi       RWX            gluster-heketi   4h

C:\Users\Maho\vagrant-glusterfs\k8s-yaml>kubectl get pv
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS    CLAIM            STORAGECLASS     REASON    AGE
pvc-d8538128-2a07-11e9-b4c1-02f6928eb0b4   10Gi       RWX            Delete           Bound     default/gvol-1   gluster-heketi             4h
```

다음은 파드에서의 마운트 확인 예다. 

```
C:\Users\Maho\vagrant-glusterfs\k8s-yaml>kubectl get po
NAME                          READY     STATUS    RESTARTS   AGE
gfs-client-5f8569b685-ljd5c   1/1       Running   0          4h
gfs-client-5f8569b685-vr7r5   1/1       Running   0          4h

C:\Users\Maho\vagrant-glusterfs\k8s-yaml>kubectl exec -it gfs-client-5f8569b685-ljd5c sh
# df -h
Filesystem                                        Size  Used Avail Use% Mounted on
overlay                                           9.7G  2.0G  7.7G  21% /
tmpfs                                              64M     0   64M   0% /dev
tmpfs                                             497M     0  497M   0% /sys/fs/cgroup
172.20.1.21:vol_05274b489f63bf6341f9bc3449d8c2ce   10G   66M   10G   1% /mnt
/dev/sda1                                         9.7G  2.0G  7.7G  21% /etc/hosts
shm                                                64M     0   64M   0% /dev/shm
tmpfs                                             497M   12K  497M   1% /run/secrets/kubernetes.io/serviceaccount
tmpfs                                             497M     0  497M   0% /proc/scsi
tmpfs                                             497M     0  497M   0% /sys/firmware
```

## 디플토 스토리지로 하기 

스토리지 클래스의 정의를 생략한 경우, GlusterFS를 기본 스토리지로 사용하도록 설정할 수 있다. 

```
$ kubectl patch storageclass gluster-heketi -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

위 설정을 통해 다음과 같이 된다. 

```
$ kubectl get storageclass
NAME                       PROVISIONER               AGE
gluster-heketi (default)   kubernetes.io/glusterfs   35m
```

## 일시 정지와 기동

`vagrant halt`로 클러스터의 가상 서버를 종료하고 `vagrant up`으로 기동한다. 


## 클린업

전부 지울 때는 다음 명령어를 실행한다. 데이터도 분실되므로 주의하도록 한다. 

```
$ vagrant destroy -f
```

## 장애 대응

GlusterFS에서는 루트 유저로 동작하지 않는 컨테이너에서 파일 시스템을 마운트하여 쓰기를 시도하면 `Permission denied` 에러가 발생한다. 이는 마운트되는 경로가 root 유저로 설정되어 있기 때문이다. 

* Bug 1312421 - glusterfs mount-point return permission denied, https://bugzilla.redhat.com/show_bug.cgi?id=1312421
* POSIX Access Control Lists, https://docs.gluster.org/en/latest/Administrator%20Guide/Access%20Control%20Lists/
* Product Documentation for Red Hat Gluster Storage 3.5, https://access.redhat.com/documentation/ja-jp/red_hat_gluster_storage/3.5/
* not able to configure with non root user #314, https://github.com/gluster/glusterfs/issues/314

레드햇(Red Hat)의 GlusterFS에서는 OpenShift v3부터 문제가 해결되었으나, 커뮤니티 버전에서는 수작업으로 대응해야 한다. 

대응 방법은 다음과 같이 k8s-yaml/chmod-pod.yml을 적용하여 일반 유저에게도 쓰기 권한을 부여하면 된다. 

```
$ kubectl get pvc (PVC명 취득)
$ vi chmod-pod.yml (PVC명을 설정)
$ kubectl apply -f chmod-pod.yml 
```

매니페스트에서는 마지막 줄의 change-me를 변경한다. 

```file:chmod-pod.yml
apiVersion: v1
kind: Pod
metadata:
  name: gfs-chmode
spec:
  containers:
  - name: change-mode
    image: alpine 
    volumeMounts:
    - name: gfs
      mountPath: /mnt
    command: [ "chmod", "a+w", "/mnt"]
  volumes:
  - name: gfs
    persistentVolumeClaim:
      claimName: <change-me>  <- PVC 이름 수정
```
