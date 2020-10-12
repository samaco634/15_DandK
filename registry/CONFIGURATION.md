# 컨테이너 레지스트리 설정 

## 로컬의 hosts파일에 등록

자체 서명된 인증서의 도메인 명으로 레지스트리 서버에 접속하기 위해서는 hosts파일에 다음 내용을 추가해야 한다. 

~~~
192.168.1.25  private.registry.local
~~~


## 자체 서명 서버 인증서 작성

~~~
$ cd auth
$ openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout domain.key -out domain.crt
Generating a 2048 bit RSA private key
.................................+++
............+++
writing new private key to 'domain.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []:JP
State or Province Name (full name) []:Tokyo
Locality Name (eg, city) []:Koto
Organization Name (eg, company) []:
Organizational Unit Name (eg, section) []:
Common Name (eg, fully qualified host name) []:private.registry.local
Email Address []:
~~~


## 유저와 패스워드 추가

~~~
docker run --rm --entrypoint htpasswd registry:v2 -Bbn dockman qwerty > auth/nginx.htpasswd
docker run --rm --entrypoint htpasswd registry:2 -Bbn fishman zxcvbn >> auth/nginx.htpasswd
~~~


## 자가서명 인증서의 등록 macOS

1. 키 체인 접근을 기동하여 다음을 선택
　　-> 키체인:시스템
　　-> 카테고리:인증서

2. auth/domain.crt 파일을 키체인의 인증서 목록에 드래그 앤 드롭 한다.

3. piravate.registry.local을 더블 클릭 한다.

4. 팝업 창의 ‘신뢰’를 확장하고, 이 인증서 사용 시 ‘항상 신뢰’를 선택한다.

5. 도커를 다시 시작한다.

6. ‘docker-compose up -d’로 레지스트리, 프록시, 프런트엔드를 기동한다.

7. 레지스트리에 로그인한다.

~~~
$ docker login -u=dockman -p=qwerty private.registry.local:5043
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
Login Succeeded
~~~


## 참고자료
https://docs.docker.com/registry/recipes/nginx/#setting-things-up


