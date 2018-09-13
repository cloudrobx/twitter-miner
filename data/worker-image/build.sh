#!/bin/sh
date > codeflag
sudo docker build --no-cache -t worker:latest .
