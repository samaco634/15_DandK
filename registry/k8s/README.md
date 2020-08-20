# Kubernetesから Private Registry をアクセスする方法


## 自己署名証明書をk8sクラスタへ登録する

Kubernetesの各サーバーに次のディレクトリを作成して、
その下に、自己署名証明書 domain.crt をコピーします。
その後、再起動は必要ありません。

~~~
# cd /etc/docker/
# mkdir -p certs.d/private.registry.local:5043
~~~


## hostsに登録

IPアドレスは、minikubeのホストであるパソコンのIPアドレスをセットします。

~~~
192.168.1.25    private.registry.local
~~~



## シークレットにユーザーとパスワードを登録

次のコマンドで、YAMLファイルを生成して、YAMLを適用します。

~~~
$ kubectl create secret docker-registry --dry-run=true \
registry-auth --docker-server=private.registry.local:5043 \
--docker-username=dockman --docker-password=qwerty \
--docker-email=xxx@yyy -o yaml > docker-secret.yml

$ kubectl apply -f docker-secret.yml 
secret "registry-auth" created
~~~


ポッドの稼働状態を確認して、対話型シェルでボッド内で操作してみます。

~~~
$ kubectl get pods
$ kubectl exec -it ubuntu bash
~~~