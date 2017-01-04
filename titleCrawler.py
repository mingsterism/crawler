from bs4 import BeautifulSoup
import requests
import lxml

def extractTitles(url):
    r = requests.get(url)
    rsoup = BeautifulSoup(r.content, 'lxml')
    titles = rsoup.find_all('a')
    for y in titles:
        print(y.text.encode('utf-8'))

extractTitles("http://www.thestar.com.my")
