FROM ubuntu:18.04
RUN apt-get update && apt-get install -y iputils-ping dnsutils curl apt-transport-https gnupg2

# install kubectl
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN touch /etc/apt/sources.list.d/kubernetes.list 
RUN echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update && apt-get install -y kubectl

# pyhon
RUN apt-get install -y python3 python-pip3
RUN pip3 install --upgrade pip
RUN pip3 install pika 
RUN pip3 install kubernetes
