# vagrant-minikube

이 Vagrant와 Ansible 코드는 VirtualBox 가상 서버 위에 Minikube를 기동하기 위한 코드다. 
Minikube는 최신 버전이 기동하도록 되어 있다. 


## Minikube 시작 방법 

가상 머신을 기동하고 로그인하여 다음 minikube를 시작하는 명령어를 실행한다. 

~~~
$ vagrant up
$ vagrant ssh
$ sudo minikube start
~~~

k8s가 기동할 때까지 10분 정도 시간이 걸린다. 다음 명령어로 모든 파드가 running하고 있으면 완료된 것이다. 

~~~
$ kubectl get pod -n kube-system
~~~

혹시 파드 중 Terminating인 것이 있다면, Minikube를 종료한 후 다시 실행해 보기 바란다. 

~~~
vagrant@minikube:~$ sudo minikube stop
Stopping local Kubernetes cluster...
Machine stopped.
vagrant@minikube:~$ sudo minikube start
Starting local Kubernetes v1.13.2 cluster...
Starting VM...
~~~


## 종료

~~~
$ sudo minikube stop
$ exit
$ vagrant halt
~~~


## 삭제

~~~
$ vagrant destroy
~~~


## 주의 사항

* 대쉬보드는 포함되지 않았다. 
* minikube delete를 한 경우에는 /usr/local/bin/minikube start --vm-driver none 로 기동한다. 

## 참고자료

* https://github.com/kubernetes/minikube
* https://kubernetes.io/docs/tasks/tools/install-minikube/#install-minikube
