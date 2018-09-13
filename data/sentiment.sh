#!/bin/sh
python sentiment.py $1 
gsutil cp $1_nlp.csv gs://isye-7406
