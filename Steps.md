# Working with K8sPodOperator

## Run airflow locally on docker container

```bash
 docker run -d -p 18080:8080 -e LOAD_EX=y puckel/docker-airflow webserver
 docker exec -it puckel /bin/bash
 docker exec -it -u 0 puckel /bin/bash

# Push image to dockerhub
 docker login docker.io
 docker image tag pyrun:latest rahulh77/pyrun:latest
 docker push rahulh77/pyrun:latest
```

## EKS steps

``` bash
https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html
Role
VPC - Subnets, Security group
EKS Cluster
Add WorkerNode Group
```
