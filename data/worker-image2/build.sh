#!/bin/sh
date > codeflag
sudo docker build --no-cache -t worker2:latest .
