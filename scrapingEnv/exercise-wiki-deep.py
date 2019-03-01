from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(url):
    global pages
    html = urlopen("http://en.wikipedia.org" + url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                href=re.compile("^/wiki/((?!:).)+$")):
        if "href" in link.attrs:
            pageLink = link.attrs['href']
            if pageLink not in pages:
                print(pageLink)
                pages.add(pageLink)
                getLinks(pageLink)

getLinks("")

