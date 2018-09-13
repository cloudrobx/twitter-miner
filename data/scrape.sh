#!/bin/sh
rm $1-$2.csv
python scrape.py $1 $2 $3 
gsutil cp $1-$2.csv gs://isye-7406
