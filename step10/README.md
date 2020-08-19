# minikube 이용시 문제 회피 방법

minikube 의 IP주소가 버전업에 따라 변하였다.
이에 따라 예제 코드 job-initiator.py에서 minikube의 IP주소를 수정해야 한다.

다음 방법으로 IP주소를 확인할 수 있다. 


~~~
$ minikube ip
192.168.64.2
~~~


다음 부분 수정

~~~
# 메시지 브로커 접속
def create_queue():
    qmgr_cred= pika.PlainCredentials('guest', 'guest')
    #qmgr_host='172.16.20.11'  # for vagrant-k8s
    #qmgr_host='192.168.99.100' # for minikube old version
    qmgr_host='192.168.64.2' # for minikube latest version <<-- 여기
    qmgr_port='31672'
    qmgr_pram = pika.ConnectionParameters(
    	      host=qmgr_host,
	      port=qmgr_port,
~~~
