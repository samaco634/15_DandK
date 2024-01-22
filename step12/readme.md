### run vitual nfs server
~~~
cd ~/15_DandK/vagrant-nfs
~~~
~~~
vagrant up
~~~

### run first persistance volume : nfs
~~~
kubectl apply -f nfs-pv.yml
~~~
