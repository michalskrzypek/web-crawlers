import requests
from bs4 import BeautifulSoup

def search_spider(max_pages):
    page = 1
    while page<=max_pages:
        url = "https://www.olx.pl/oferty/q-buty-nike/?page="+str(page)
        source_code = requests.get(url)
        txt = source_code.text
        soup = BeautifulSoup(txt)
        for link in soup.findAll('a', {"class": "marginright5 link linkWithHash detailsLink"}):
            href= link.get('href')
            title = link.strong.string
            print (href)
            print(title)
        page=page+1

search_spider(1)

