#!/bin/sh
kubectl delete job workers
kubectl apply -f job-worker.yaml
