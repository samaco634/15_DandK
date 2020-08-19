# Step09 서비스 보충 


## ExtenalName 외부 DNS 주소 해결 예

v1.13이후, extenalName에 IP주소를 기술할 수 있으나 DNS의 문자열로 인식된다. 
따라서 매니페스트에 DNS 이름을 써서 접속해야 한다. 


실행예 svc-ext-dns.yml

~~~
$ kubectl apply -f svc-ext-dns.yml
service/yahoo created

$ kubectl get svc
NAME         TYPE           CLUSTER-IP   EXTERNAL-IP       PORT(S)   AGE
kubernetes   ClusterIP      10.96.0.1    <none>            443/TCP   5d2h
yahoo        ExternalName   <none>       www.yahoo.co.jp   <none>    15s

$ kubectl run -it bustbox --restart=Never --rm --image=busybox sh
If you don't see a command prompt, try pressing enter.
/ # ping yahoo
PING yahoo (183.79.217.124): 56 data bytes
64 bytes from 183.79.217.124: seq=0 ttl=61 time=16.367 ms
64 bytes from 183.79.217.124: seq=1 ttl=61 time=16.493 ms
64 bytes from 183.79.217.124: seq=2 ttl=61 time=16.939 ms
64 bytes from 183.79.217.124: seq=3 ttl=61 time=16.449 ms
^C
--- yahoo ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 16.367/16.562/16.939 ms
~~~



## 헤드리스로 IP주소를 하드코딩하는 

헤드리스 서비스와 엔드포인트를 svc-headless.yml에 작성한다. 
Endpoint의 매니페스트를 작성하여 그 안에 IP주소를 하드코딩하고, 오브젝트 명은 서비스 엔드포인트와 일치해야 한다. 


실행예 svc-headless.yml

~~~
$ kubectl apply -f svc-headless.yml
endpoints/server1 created
service/server1 created

$ kubectl get svc
NAME         TYPE           CLUSTER-IP   EXTERNAL-IP       PORT(S)   AGE
server1      ClusterIP      None         <none>            <none>    7s

$ kubectl get ep
NAME         ENDPOINTS             AGE
server1      192.168.1.16          13s

$ kubectl run -it busybox --restart=Never --rm --image=busybox sh
If you don't see a command prompt, try pressing enter.
/ # ping server1
PING server1 (192.168.1.16): 56 data bytes
64 bytes from 192.168.1.16: seq=0 ttl=61 time=0.754 ms
64 bytes from 192.168.1.16: seq=1 ttl=61 time=0.905 ms
64 bytes from 192.168.1.16: seq=2 ttl=61 time=0.585 ms
^C
--- server1 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.585/0.748/0.905 ms~
~~~

