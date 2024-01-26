1.24 버전 이후의 k8s를 사용한 클러스터로 작업중이라면 ServiceAccount와 함께 수동으로 Token을 위한 Secret을 생성해야 합니다. 
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount
~~~
kubectl apply -f secret.yml
~~~
