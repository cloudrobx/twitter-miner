# Set the base image
FROM ubuntu
# Dockerfile author / maintainer 
MAINTAINER Name romartin@google.com
# Update application repository list  
RUN apt-get update && apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y git
RUN apt-get install -y lsb-release
RUN apt-get install -y curl
RUN pip install --upgrade pip 
RUN pip install --upgrade virtualenv
RUN pip install twitterscraper
RUN pip install unicodecsv
RUN pip install python-dateutil
RUN pip install google-cloud
RUN git clone https://github.com/taspinar/twitterscraper.git
WORKDIR twitterscraper
RUN python setup.py install
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && apt-get install -y google-cloud-sdk
RUN apt-get install -y nano
ADD codeflag / 
RUN git clone https://github.gatech.edu/rmartin95/ISYE7406.git
