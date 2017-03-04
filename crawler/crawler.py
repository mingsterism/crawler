import requests
from lxml import html
from collections import deque
import argparse
from bs4 import BeautifulSoup
from readability.readability import Document

class Site:
    def __init__(self, requests_result):
        self.url = requests_result.url
        self.headers = requests_result.headers
        self.content = requests_result.content
        self.base_url = requests_result.url
        self.dq = deque()
        self.crawled = set()  

    def base_info(self):
        info = {'url': self.url, 'headers': self.headers}
        return info

class Actions:
    @staticmethod
    def _get_href(url):
        """ Private function that accepts a URL string and returns a list of href"""
        result = requests.get(url)
        content = result.content 
        elements = html.fromstring(content)
        return elements.xpath('//a/@href')

    @staticmethod
    def process_urls(site):
        """ Accepts a site object and returns a site object. 
        site object is a requests.get() object. eg: siteObject = requests.get(url)
        Will add list of urls into object.dq and object.crawled deque() and set() respectively.
        """
        href_results = Actions._get_href(site.url)
        href_results = [h.strip() for h in href_results]

        # Fix bug for relative urls:
        hrefs = [site.base_url + h if h.startswith('/') and len(h) > 1 else h for h in href_results]

        # Now filter out those here only
        hrefs = [h for h in hrefs if h.startswith(site.base_url)]

        for href in hrefs:
            if href not in site.crawled:
                site.dq.appendleft(href)
                site.crawled.add(href)
            else:
                pass  
        return site

    @staticmethod 
    def add_result_to_file(result, file):
        with open(file, 'w') as file_:
            file_.write(result)

    @staticmethod
    def _cleanText(text):
        REGEX = re.compile(r'(<.*?>|\t|\n)')
        return re.sub(REGEX, "", text)

    @staticmethod
    def getArticle(url):
        """ Accepts a url and returns a string 
        containing the article body of the url"""
        r = requests.get(url)
        r_content = r.content
        article = Document(r_content).summary()
        return Actions._cleanText(article) 

