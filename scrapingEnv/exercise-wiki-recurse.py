from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

url = "/wiki/Kevin_Bacon"
random.seed(datetime.datetime.now())

def getLinks(url):
    url = "http://en.wikipedia.org" + url;
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", 
    {"href":re.compile("^/wiki/((?!:).)+$")})

links = getLinks(url)
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

