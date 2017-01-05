FROM ubuntu:16.04
MAINTAINER ming.k@hotmail.com
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev gcc libffi-dev
RUN apt-get -y install python3-pip
RUN pip3 install lxml
RUN pip3 install requests
RUN apt-get -y install build-essential
RUN pip3 install Cython
RUN pip3 install pybloomfiltermmap3
RUN pip3 install beautifulsoup4
RUN apt-get -y install vim && apt-get -y install git
RUN git clone https://github.com/mingsterism/crawler

