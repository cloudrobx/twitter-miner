#!/bin/sh
gcloud beta container clusters resize cluster-2 -q --node-pool default-pool --size 5 --zone=us-central1-a
