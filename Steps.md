# Working with K8sPodOperator

## Run airflow locally on docker container

```bash
 docker run -d -p 18080:8080 -e LOAD_EX=y -v "$(pwd):/usr/local/airflow/dags" --name mypuckel puckel/docker-airflow webserver
 docker exec -it puckel /bin/bash
 docker exec -it -u 0 puckel /bin/bash

 apt-get update
 apt-get install vim
 pip install kubernetes

 vi airflow.cfg (user airflow)
 hide_paused_dags_by_default = True
 docker cp ~/.kube mypuckel:/usr/local/airflow
 chown -R airflow:airflow /usr/local/airflow/.kube/
 docker restart mypuckel

# Push image to dockerhub
 docker login docker.io
 docker image tag pyrun:latest rahulh77/pyrun:latest
 docker push rahulh77/pyrun:latest
# run
docker run --rm -it --name rahulh77/pyruncon pyrun 10
```

## EKS steps

``` bash
https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html
Role
VPC - Subnets, Security group
EKS Cluster
Add WorkerNode Group
```
