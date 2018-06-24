# Get the image
FROM python:2.7

MAINTAINER Parikshit Yadav <parikshit979@gmail.com>

# Install apt packages
RUN apt-get update && apt-get install -y python-dev && apt-get install -y python-pip \
    && apt-get install -y default-libmysqlclient-dev && apt-get install -y supervisor \
    && apt-get install -y python-setuptools

# Copy services supervisor config files
COPY ./shortner.conf /etc/supervisor/conf.d/shortner.conf

# Add source code
ADD . /UrlShortner/

COPY ./requirements.txt /UrlShortner/requirements.txt

WORKDIR /UrlShortner/

RUN pip install --upgrade setuptools pip
RUN pip install -r requirements.txt
