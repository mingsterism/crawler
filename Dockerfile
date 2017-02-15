FROM ubuntu:16.04
MAINTAINER ming.k@hotmail.com
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python-pip
RUN apt-get install git -y
RUN git clone https://github.com/mingsterism/crawler /home/crawl


ENV crawlerDir /home/crawl
WORKDIR $crawlerDir
RUN pwd
RUN ls .
RUN pip install -e .
ARG url
ENTRYPOINT crawl launch --verbose $url
#RUN crawl launch --verbose $url
#RUN ["crawl", "launch", "--verbose", "http://www.thestar.com.my"]
