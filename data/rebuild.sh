#!/bin/sh
cd collector-image
./build.sh
./push.sh
cd ..
cd worker-image
./build.sh
./push.sh
cd ..
cd worker-image2
./build.sh
./push.sh
cd ..

