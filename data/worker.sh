#!/bin/sh
python worker.py
gsutil cp /twitterscraper/ISYE7406/data/*.csv gs://isye-7406/
