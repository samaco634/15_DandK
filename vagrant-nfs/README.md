# vagrant-nfs

이 Vagrant와  Ansible 코드는 가상 서버에 NFS 서버를 구축하여 쿠버네티스 클러스터의 파드에서 마운트할 수 있게 하기 위한 코드다. 이 가상 서버의 IP 주소는 가상 서버에 할당되는 내부 통신용 주소다. 

1. nfsserver 172.20.1.10

쿠버네티스 클러스터와 조합하여 퍼시스턴트 볼륨을 수동으로 프로비저닝하는 환경을 구축할 수 있다. 


## 필요한 소프트웨어

* Vagrant (https://www.vagrantup.com/)
* VirtualBox (https://www.virtualbox.org/)
* kubectl (https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* git (https://kubernetes.io/docs/tasks/tools/install-kubectl/)


## 가상 머신의 호스트 환경

Vagrant와 VirtualBox가 기동하는 OS가 필요하다. 

* Windows10　
* MacOS
* Linux

필자의 테스트 환경

* RAM: 8GB
* 남은 저장 공간: 5GB 
* CPU: Intel Core i5



## NFS 서버 시작

다음 명령어를 통해 가상 서버가 VirtualBox의 LAN 위에 기동한다. 

```
$ vagrant up
```


## 쿠버네티스 파드에서의 이용

k8s-yaml 매니페스트를 적용한다. 

```
kubectl apply -f nfs-pv.yml (NFS 서버 접속)
kubectl apply -f nfs-pvc.yml (Persistent Volume Claim으로 NFS의 추상화 PV와 접속)
kubectl apply -f nfs-client.yml (NFS를 마운트하는 파드 2개 기동)
```


## 일시 정지와 기동

vagrant halt로 가상 서버를 종료하고, vagrant up을 하면 다시 기동한다.



## 클린업

전부 삭제하기 위해서는 다음 명령어를 실행한다. 데이터도 삭제되므로 주의한다. 

```
$ vagrant destroy
```
