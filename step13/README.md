# Ingress 컨트롤러 + Keepalived 동작 확인 보충


마스터 노드에서 kubectl을 실행하여 동작을 확인하는 예

~~~
vagrant@master:~$ git clone https://github.com/takara9/codes_for_lessons
~~~


## Ingress Controller + Keepalived 매니페스트 적용

~~~
vagrant@master:~/codes_for_lessons/step13$ kubectl apply -f ingress-keepalived/
namespace/tkr-system created
configmap/nginx-configuration created
configmap/tcp-services created
configmap/udp-services created
deployment.apps/nginx-ingress-controller created
service/nginx-ingress-svc created
deployment.extensions/default-http-backend created
service/default-http-backend created
serviceaccount/nginx-ingress-serviceaccount created
clusterrolebinding.rbac.authorization.k8s.io/nginx-ingress-clusterrole-nisa-binding created
configmap/vip-configmap created
daemonset.extensions/kube-keepalived-vip created
serviceaccount/kube-keepalived-vip created
clusterrole.rbac.authorization.k8s.io/kube-keepalived-vip created
clusterrolebinding.rbac.authorization.k8s.io/kube-keepalived-vip created
~~~

## 기동까지 대기하는 상태와 기동 완료 상태 

~~~
vagrant@master:~/codes_for_lessons/step13$ kubectl get pod -n tkr-system -w
NAME                                        READY   STATUS              RESTARTS   AGE
default-http-backend-675897b6d8-kpl4v       0/1     ContainerCreating   0          13s
kube-keepalived-vip-cdm9g                   0/1     ContainerCreating   0          12s
kube-keepalived-vip-hxr4v                   0/1     ContainerCreating   0          12s
nginx-ingress-controller-797f965f47-lhwnl   0/1     ContainerCreating   0          13s
kube-keepalived-vip-cdm9g                   1/1     Running             0          13s
kube-keepalived-vip-cdm9g                   0/1     Completed           0          20s
kube-keepalived-vip-cdm9g                   1/1     Running             1          22s
nginx-ingress-controller-797f965f47-lhwnl   1/1     Running             0          29s
kube-keepalived-vip-cdm9g                   0/1     Completed           1          28s
default-http-backend-675897b6d8-kpl4v       1/1     Running             0          32s
kube-keepalived-vip-hxr4v                   1/1     Running             0          41s
kube-keepalived-vip-cdm9g                   0/1     CrashLoopBackOff    1          43s
kube-keepalived-vip-cdm9g                   1/1     Running             2          44s
^C

vagrant@master:~/codes_for_lessons/step13$ kubectl get pod -n tkr-system 
NAME                                        READY   STATUS    RESTARTS   AGE
default-http-backend-675897b6d8-kpl4v       1/1     Running   0          15m
kube-keepalived-vip-cdm9g                   1/1     Running   2          15m
kube-keepalived-vip-hxr4v                   1/1     Running   0          15m
nginx-ingress-controller-797f965f47-lhwnl   1/1     Running   0          15m
~~~

## Ingress를 사용하는 애플리케이션 기동

~~~
vagrant@master:~/codes_for_lessons/step13$ kubectl apply -f test-apl/
deployment.apps/hello-world-deployment created
service/hello-world-svc created
ingress.extensions/hello-world-ingress created
~~~

## 애플리케이션 기동 확인

~~~
vagrant@master:~/codes_for_lessons/step13$ kubectl get ing
NAME                  HOSTS            ADDRESS   PORTS   AGE
hello-world-ingress   abc.sample.com             80      4s

vagrant@master:~/codes_for_lessons/step13$ kubectl get pod
NAME                                    READY   STATUS              RESTARTS   AGE
hello-world-deployment-88fd567c-h497j   0/1     ContainerCreating   0          8s
hello-world-deployment-88fd567c-kd455   0/1     ContainerCreating   0          8s
hello-world-deployment-88fd567c-mwg2b   0/1     ContainerCreating   0          8s
hello-world-deployment-88fd567c-s74rz   0/1     ContainerCreating   0          8s
hello-world-deployment-88fd567c-x9ttx   0/1     ContainerCreating   0          8s

vagrant@master:~/codes_for_lessons/step13$ kubectl get pod
NAME                                    READY   STATUS    RESTARTS   AGE
hello-world-deployment-88fd567c-h497j   1/1     Running   0          66s
hello-world-deployment-88fd567c-kd455   1/1     Running   0          66s
hello-world-deployment-88fd567c-mwg2b   1/1     Running   0          66s
hello-world-deployment-88fd567c-s74rz   1/1     Running   0          66s
hello-world-deployment-88fd567c-x9ttx   1/1     Running   0          66s
~~~


## curl명령어로 접근 테스트

DNS나 hosts에 등록하지 않고, curl의 헤더에 도메인명을 설정하면 Ingress가 인식한다. 

~~~
vagrant@master:~$ curl --header "Host: abc.sample.com" http://172.16.20.99/
<html><head><title>HTTP Hello World</title></head><body><h1>Hello from hello-world-deployment-88fd567c-h497j</h1></body></html
~~~


## 주의

이 매니페스트는 K8s 1.14 버전에서 확인했으며, 이 후 버전에서의 동작은 보장하지 않는다.