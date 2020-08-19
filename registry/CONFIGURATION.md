# コンテナ・レジストリのコンフィグレーション

## ローカルのhostsファイルへの登録

自己署名証明書のドメイン名で、レジストリサーバーをアクセスできる様に、
hostsファイルに次のエントリを追加します。

~~~
192.168.1.25  private.registry.local
~~~


## 自己署名のサーバー証明書の作成

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


## ユーザーとパスワードの追加

~~~
docker run --rm --entrypoint htpasswd registry:v2 -Bbn dockman qwerty > auth/nginx.htpasswd
docker run --rm --entrypoint htpasswd registry:2 -Bbn fishman zxcvbn >> auth/nginx.htpasswd
~~~


##  自己署名証明書の登録 macOS

1. キーチェーンアクセスを起動して、以下を選択する
　　-> キーチェーン:システム
　　-> 分類:証明書

2. auth/domain.crt ファイルを キーチェーンの証明書リストへ、ドラッグ＆ドロップ

3. piravate.registry.local をクリック

4. ポップアップしたウィンドの「信頼」を展開
   そして、この証明書を利用する時: 「常に信頼」を選択

5. Dockerを再起動

6. docker-compose up -d で、レジストリ、プロキシ、フロントエンドを起動

7. レジストリへログイン

~~~
$ docker login -u=dockman -p=qwerty private.registry.local:5043
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
Login Succeeded
~~~







## 参考資料
https://docs.docker.com/registry/recipes/nginx/#setting-things-up


