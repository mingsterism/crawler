import requests
from lxml import html
from collections import deque
from pybloomfilter import BloomFilter
import argparse

class Site:
    def __init__(self, r_site):
        self.url = r_site.url
        self.headers = r_site.headers
        self.content = r_site.content
        self.base_url = r_site.url
        self.dq = deque()
        self.crawled = BloomFilter(1000000, 0.01, 'filter-bloom')
    def baseInfo(self):
        info = {'url': self.url, 'headers': self.headers}
        return info

class Actions:
    @staticmethod
    def getHref(url):
        r = requests.get(url)
        c = r.content 
        elements = html.fromstring(c)
        return elements.xpath('//a/@href')
    @staticmethod
    def processUrls(url, object):
        hrefs = Actions.getHref(url)
        for x in hrefs:
            if object.base_url in x and x not in object.dq and x not in object.crawled:
                object.dq.appendleft(x)
                print(x)
            continue
        return object.dq
   
def recurseCrawl(url, object):
    if (len(object.dq) != 0): 
        nextUrl = object.dq.pop()
        Actions.processUrls(nextUrl)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, help="enter a url to crawl")
    args = parser.parse_args()
    url = args.url.strip()
    r = requests.get(url)
    a1 = Site(r)
    print(Actions.processUrls(url, a1))
    while(len(a1.dq)!= 0):
        nxtUrl = a1.dq.pop().strip()
        Actions.processUrls(nxtUrl, a1)
        a1.crawled.add(nxtUrl.rstrip())













