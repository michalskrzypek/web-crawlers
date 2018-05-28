import requests
from bs4 import BeautifulSoup
import operator


def words_counter(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for auction_text in soup.findAll('a', {'class': 'marginright5 link linkWithHash detailsLink'}):
        content = auction_text.strong.string
        single_words = content.lower().split()
        for word in single_words:
            word_list.append(word)
    clean_list(word_list)




def clean_list(list_of_words):
    clean_word_list = []
    for each_word in list_of_words:
        symbol = '~!@#$%^&*()_+-=[]{},.?:;/\'\"'
        for i in range (0, len(symbol)):
            each_word = each_word.replace(symbol[i], "")
        if len(each_word) >0:
            clean_word_list.append(each_word)
    counter(clean_word_list)


def counter(some_clean_list):
    sorted_list={}
    for word in some_clean_list:
        if word in sorted_list:
            sorted_list[word] += 1
        else:
            sorted_list[word] = 1
    for key, value in sorted (sorted_list.items(), key = operator.itemgetter(1)):
        print (key, value)


words_counter('https://www.olx.pl/dla-dzieci/zabawki/')

