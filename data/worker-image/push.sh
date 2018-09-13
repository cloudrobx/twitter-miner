#!/bin/sh
docker tag worker gcr.io/isye-7406/worker:latest
gcloud docker -- push gcr.io/isye-7406/worker
