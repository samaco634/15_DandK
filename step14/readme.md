# hpa 생성 - 선언형 명령
~~~
kubectl apply -f hpa.yaml
~~~
# hpa 생성 - 명령형 명령
~~~
kubectl autoscale deployment heavy-cal --cpu-percent=50 --min=1 --max=50
~~~
# hpa 
~~~
kubectl get hpa
~~~
 > NAME        REFERENCE                   TARGET    MINPODS  MAXPODS   REPLICAS   AGE  
 > heavy-cal   Deployment/heavy-cal/scale  0% / 50%  1        50        1          18s
