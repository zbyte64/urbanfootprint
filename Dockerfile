# We need an init system for current UF configuration
# so we're using phusion's Ubuntu 140.04 baseimage
# needs libgdal1-dev
# FROM phusion/baseimage:18.04-1.0.0-amd64
# cant pip install things: (too old)
# FROM ubuntu:20.04
FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

# Set the locale
# RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# webserver
RUN apt-get update && apt-get install -y \
        build-essential \
        curl \
        git \
        graphviz \
        graphviz-dev \
        libevent-dev \
        libfreetype6-dev \
        libpq-dev 

# python
RUN apt-get install -y \
        python3-pip \
        python3-dev

# spatial
RUN apt-get install -y \
        python3-gdal \
        libproj-dev \
        gdal-bin \
        libgdal-dev


RUN apt-get install -y \
        postgresql-client

# RUN apt-get install -y wget
# RUN python -m pip install --upgrade pip
# RUN wget https://files.pythonhosted.org/packages/3f/08/7347ca4021e7fe0f1ab8f93cbc7d2a7a7350012300ad0e0227d55625e2b8/pip-1.5.6-py2.py3-none-any.whl#sha256=fbc1351ffedf09ca7560428758845a88d648b9730b63ce9e5df53a7c89f039a4
# RUN pip install -U ./pip-1.5.6-py2.py3-none-any.whl 
# RUN apt-get install libgdal-dev
# RUN pip install ansible==1.9.6

# Add playbooks to the Docker image
RUN mkdir -p /opt/urbanfootprint/
ADD ./requirements.txt /opt/urbanfootprint/requirements.txt
WORKDIR /opt/urbanfootprint

RUN pip install -U -r requirements.txt

ADD . /opt/urbanfootprint
# CMD ["/sbin/my_init"]
