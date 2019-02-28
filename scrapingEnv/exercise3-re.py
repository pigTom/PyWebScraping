from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for img in bsObj.findAll("img", {"src":re.compile("\.\./img/gifts/img.*\.jpg")}):
    print(img.attrs)
