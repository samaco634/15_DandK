# docker-composeを使用しないで起動する方法

docker network create backend-network


docker run -d --network backend-network --name registry -p 5000:5000 -v `pwd`/data:/var/lib/registry registry:2

docker run -d --network backend-network --name nginx -p 5043:443 -v `pwd`/auth:/etc/nginx/conf.d -v `pwd`/auth/nginx.conf:/etc/nginx/nginx.conf:ro nginx:alpine

docker run -d --network backend-network --name regweb -p 9080:80 -e ENV_DOCKER_REGISTRY_HOST=private.registry.local -e ENV_DOCKER_REGISTRY_PORT=5043 -e ENV_DOCKER_REGISTRY_USE_SSL=1 konradkleine/docker-registry-frontend:v2



