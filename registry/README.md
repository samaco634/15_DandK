# Docker Container Private Registry

## 사전 준비


### hosts파일에 등록 

自己署名証明書のドメイン名で、レジストリサーバーをアクセスできる様に、パソコンのhostsファイルに、次のエントリを追加します。このIPアドレスは、自パソコンのIPアドレスですから、各自のDHCP等でアサインされているIPアドレスに置き換えてください。

~~~
192.168.1.25  private.registry.local
~~~

### 자가서명 인증서의 등록 macOS

1. 키 체인 접근을 기동하여 다음을 선택
　　-> 키체인:시스템
　　-> 카테고리:인증서

2. auth/domain.crt 파일을 키체인의 인증서 목록에 드래그 앤 드롭 한다.

3. piravate.registry.local을 더블 클릭 한다.

4. 팝업 창의 ‘신뢰’를 확장하고, 이 인증서 사용 시 ‘항상 신뢰’를 선택한다.

5. 도커를 다시 시작한다.

## 레지스트리 시작

~~~
docker-compose up -d
~~~


## 테스트

레지스트리 로그인

~~~
$ docker login -u=dockman -p=qwerty private.registry.local:5043
~~~


컨테이너 Push

~~~
$ docker pull ubuntu:18.04
$ docker tag ubuntu:18.04 private.registry.local:5043/ubuntu:18.04
$ docker push private.registry.local:5043/ubuntu:18.04
~~~


브라우저에서 http://localhost:9080/ 에 접속
유저ID dockman、비밀번호 qwerty 로 리포지터리가 표시됨



컨테이너 실행

~~~
$ docker run -it private.registry.local:5043/ubuntu:18.04 bash
root@ff1eedb30e1c:/# cat /etc/issue
Ubuntu 18.04.1 LTS \n \l

root@ff1eedb30e1c:/# uname -a
Linux ff1eedb30e1c 4.9.60-linuxkit-aufs #1 SMP Mon Nov 6 16:00:12 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
~~~



## 레지스트리 정지

~~~
docker-compose down
~~~



## 참고자료
* [1] docker docs, Authenticate proxy with nginx, https://docs.docker.com/registry/recipes/nginx/
* [2] https://github.com/kwk/docker-registry-frontend
* [3] https://hub.docker.com/_/registry/

