#!/bin/sh
docker tag collector gcr.io/isye-7406/collector:latest
gcloud docker -- push gcr.io/isye-7406/collector
