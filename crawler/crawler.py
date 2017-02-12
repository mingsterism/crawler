import requests
from lxml import html
from collections import deque
from pybloomfilter import BloomFilter
import argparse
from bs4 import BeautifulSoup

class Site:
    def __init__(self, requests_result):
        self.url = requests_result.url
        self.headers = requests_result.headers
        self.content = requests_result.content
        self.base_url = requests_result.url
        self.dq = deque()
        self.crawled = BloomFilter(1000000, 0.01, 'filter-bloom')

    def base_info(self):
        info = {'url': self.url, 'headers': self.headers}
        return info

class Actions:

    @staticmethod
    def get_href(url):
        result = requests.get(url)
        content = result.content 
        elements = html.fromstring(content)
        return elements.xpath('//a/@href')

    @staticmethod
    def process_urls(url, site):
        hrefs = Actions.get_href(url)
        for x in hrefs:
            if (site.base_url in x or "http" + site.base_url[5:] in x) and x not in site.dq and x not in site.crawled:
                site.dq.appendleft(x)
                #print(x)
            continue
        return site.dq

    @staticmethod
    def extract_titles(url):
        result = requests.get(url)
        rsoup = BeautifulSoup(result.content, 'lxml')
        titles = rsoup.find_all('a')
        for y in titles:
            print(y.text.encode('utf-8'))
   

