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
            #print (href)
            #print(title)
            get_single_item_data(href)
        page=page+1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    txt = source_code.text
    soup = BeautifulSoup(txt)
    for item_name in soup.findAll('div', {"class": "offer-titlebox"}):
        name = item_name.h1.string
        #print (name)
    for item_price in soup.findAll('div', {'class': 'price-label'}):
        price = item_price.strong.string
        #print (price)
    print(name+"Cena: "+ price)
    for item_condition in soup.findAll('td', {'class': 'value'}):
        condition = item_condition.strong.a.string
        print (condition)




search_spider(1)

