# 실습용 예제 코드

이 리포지터리는 도서 《15단계로 배우는 도커와 쿠버네티스》의 예제 코드입니다. 

## 책 목차

책에서 다루는 스텝(step)별로 디렉터리를 구성하였습니다. 특정 스텝은 예제 코드가 없는 경우가 있습니다. 

### 2장 컨테이너 개발을 익히기 위한 5단계
* Step01 컨테이너 첫 걸음(예제 코드 없음)
* Step02 컨테이너 조작(예제 코드 없음)
* Step03 컨테이너 개발
* Step04 컨테이너와 네트워크 
* Step05 컨테이너 API

### 3장 K8s 실전 활용을 위한 10단계
* Step06 Kubernetes 첫걸음(예제 코드 없음)
* Step07 매니페스트와 파드
* Step08 디플로이먼트
* Step09 서비스
* Step10 잡과 크론잡
* Step11 스토리지
* Step12 스테이트풀셋
* Step13 인그레스
* Step14 오토스케일
* Step15 클러스터 가상화


## 실행 환경

IKS나 GKE와 같은 퍼블릭 클라우드에서도 동작합니다. 혹은 독자의 PC에 VirtualBox와 Vagrant를 사용하여 학습 환경을 구축해도 됩니다.

* Minikube https://github.com/takara9/vagrant-minikube 
* Kubernetes https://github.com/Jpub/15_DandK/tree/master/vagrant-kubernetes 

쿠버네티스와 연동할 수 있는 저장소

* NFS 서버 일반적인 NFS 서버를 컨테이너에서 마운트하는 경우 https://github.com/takara9/vagrant-nfs
* GlusterFS 서버 + Heketi 동적 프로비저닝 환경 https://github.com/Jpub/15_DandK/tree/master/vagrant-glusterfs


즐겁게 도커와 쿠버네티스를 학습하기 바랍니다.