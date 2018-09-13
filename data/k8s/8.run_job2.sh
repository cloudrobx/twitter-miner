#!/bin/sh
kubectl delete job workers2
kubectl apply -f job-worker2.yaml
