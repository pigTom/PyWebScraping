from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(url):
    global pages
    html = urlopen(prefix + url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a",
                href=re.compile("^/pig[tT]om(/[^/]+)?$")):
        if "href" in link.attrs:
            pageLink = link.attrs['href']
            if pageLink not in pages:
                print(pageLink)
                pages.add(pageLink)
                getLinks(pageLink)
prefix = "http://github.com"
url = "/pigtom"
getLinks(url)

