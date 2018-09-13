#!/bin/sh
docker tag worker2 gcr.io/isye-7406/worker2:latest
gcloud docker -- push gcr.io/isye-7406/worker2
