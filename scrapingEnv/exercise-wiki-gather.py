from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(url):
    global pages
    html = urlopen("http://en.wikipedia.org" + url)
    bsObj = BeautifulSoup(html)
    try:
        # this is a comment
        # print head of the article
        print(bsObj.h1.get_text())
        # find first paragraph 
        # print(bsObj.find(id="mw-content-text").findAll("p")[0])
        # edit links occurs only on articles
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a",
                href=re.compile("^/wiki/((?!:).)+$")):
        if "href" in link.attrs:
            pageLink = link.attrs['href']
            if pageLink not in pages:
                print("-------------------\n" + pageLink)
                pages.add(pageLink)
                getLinks(pageLink)

getLinks("")

