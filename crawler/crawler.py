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
        self.crawled = set()  # BloomFilter(1000000, 0.01, 'filter-bloom')

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
        href_results = Actions.get_href(url)
        href_results = [h.strip() for h in href_results]

        # Fix bug for relative urls:
        hrefs = [site.base_url + h if h.startswith('/') and len(h) > 1 else h for h in href_results]

        # Now filter out those here only
        hrefs = [h for h in hrefs if h.startswith(site.base_url)]

        for href in hrefs:
            if href not in site.crawled:
                with open('/tmp/crawled.txt', 'w') as file_:
                    file_.write(href + '\n')
                site.dq.appendleft(href)
                site.crawled.add(href)
            else:
                pass  # print("NOT appending {}".format(href))
        return site.dq

    @staticmethod
    def extract_titles(url):
        result = requests.get(url)
        rsoup = BeautifulSoup(result.content, 'lxml')
        titles = rsoup.find_all('a')
        for y in titles:
            print(y.text.encode('utf-8'))
   

