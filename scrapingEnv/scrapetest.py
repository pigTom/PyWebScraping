from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), features="html.parser");
# print(bsObj.h1)
# print(bsObj.div)
# print(bsObj.html.body.div)
# print(bsObj.title)

