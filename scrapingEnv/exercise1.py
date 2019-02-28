from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read(), features="html.parser");
print(bsObj.h1)
# print(bsObj.div)
# print(bsObj.html.body.div)
# print(bsObj.title)

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser");
        nameList = bsObj.findAll("span", {"class":"green"})
        for name in nameList:
            print(name.get_text())
        title = bsObj.body.title
    except AtrributeError as e:
        print(e)
        return None
    return title

url = "http://www.pythonscraping.com/pages/warandpeace.html"
# title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
title = getTitle(url)
if title == None:
    print("title could not be found")
else:
    print(title)
