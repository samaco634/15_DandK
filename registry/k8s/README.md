# Kubernetes에서 Private Registry에 접속하는 방법


## 자체 서명한 인증서를 k8s클러스터에 등록

쿠버네티스의 각 서버에 다음 디렉터리를 작성하여 그 밑에 자체 서명 인증서 domain.crt를 복사한다. 
재기동은 필요하지 않다. 

~~~
# cd /etc/docker/
# mkdir -p certs.d/private.registry.local:5043
~~~


## hosts에 등록

IP주소는 minikube의 호스트 PC의 IP주소를 설정한다. 

~~~
192.168.1.25    private.registry.local
~~~

## 스크릿에 유저와 패스워드 등록

다음 명령어로, YAML파일을 생성하여 YAML을 적용

~~~
$ kubectl create secret docker-registry --dry-run=true \
registry-auth --docker-server=private.registry.local:5043 \
--docker-username=dockman --docker-password=qwerty \
--docker-email=xxx@yyy -o yaml > docker-secret.yml

$ kubectl apply -f docker-secret.yml 
secret "registry-auth" created
~~~

파드의 가동 상태를 확인하여 대화형 쉘로 파드에 접속한다. 

~~~
$ kubectl get pods
$ kubectl exec -it ubuntu bash
~~~