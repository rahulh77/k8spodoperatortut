# 
## Useful commands

``` bash

# Connect to eks cluster
aws eks --region <region> update-kubeconfig --name <cluster_name>
or
aws eks --region <region> update-kubeconfig --name <cluster_name> --profile <profile_name>


kubectl apply -f pyrun_pod.yaml && kubectl get pods -w
kubectl describe pod/pyrun-pod
kubectl logs pod/pyrun-pod

kubectl delete pod/pyrun-pod
```

``` bash
kubectl apply -f pyrun_job.yaml --watch

# ttlSecondsAfterFinished does not work as intended
kubectl delete job pyrun-job
```
