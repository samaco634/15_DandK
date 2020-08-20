# Docker Container Private Registry

## 事前準備事項


### hostsファイルへの登録

自己署名証明書のドメイン名で、レジストリサーバーをアクセスできる様に、パソコンのhostsファイルに、次のエントリを追加します。このIPアドレスは、自パソコンのIPアドレスですから、各自のDHCP等でアサインされているIPアドレスに置き換えてください。

~~~
192.168.1.25  private.registry.local
~~~


###  自己署名証明書の登録 macOS

自己署名証明書のエラーを回避するため、自己署名証明書をMacのキーチェーンへ登録します。


1. キーチェーンアクセスを起動して、以下を選択する
　　-> キーチェーン:システム
　　-> 分類:証明書

2. auth/domain.crt ファイルを キーチェーンの証明書リストへ、ドラッグ＆ドロップ

3. piravate.registry.local をクリック

4. ポップアップしたウィンドの「信頼」を展開
   そして、この証明書を利用する時: 「常に信頼」を選択

5. Dockerを再起動




## レジストリの開始

~~~
docker-compose up -d
~~~


## テスト

レジストリへログイン

~~~
$ docker login -u=dockman -p=qwerty private.registry.local:5043
~~~


コンテナのPush

~~~
$ docker pull ubuntu:18.04
$ docker tag ubuntu:18.04 private.registry.local:5043/ubuntu:18.04
$ docker push private.registry.local:5043/ubuntu:18.04
~~~


ブラウザで、http://localhost:9080/ をアクセス
ユーザーID dockman、パスワード qwerty でリポジトリが表示される。



コンテナの実行

~~~
$ docker run -it private.registry.local:5043/ubuntu:18.04 bash
root@ff1eedb30e1c:/# cat /etc/issue
Ubuntu 18.04.1 LTS \n \l

root@ff1eedb30e1c:/# uname -a
Linux ff1eedb30e1c 4.9.60-linuxkit-aufs #1 SMP Mon Nov 6 16:00:12 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
~~~



## レジストリの停止

~~~
docker-compose down
~~~



## 参考資料
* [1] docker docs, Authenticate proxy with nginx, https://docs.docker.com/registry/recipes/nginx/
* [2] https://github.com/kwk/docker-registry-frontend
* [3] https://hub.docker.com/_/registry/

