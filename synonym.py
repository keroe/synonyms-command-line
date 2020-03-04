#!/usr/bin/python
import requests
import bs4
import re

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://synonyme.woxikon.de/synonyme/'

try:
    wort = sys.argv[1]
except IndexError:
    print("Usage: synonym word")
    exit()
url += wort + ".php"
res = requests.get(url)
res.raise_for_status()
html = bs4.BeautifulSoup(res.text, "html.parser")

all_synonyms = html.find_all("div", {"class": "upper-synonyms"})
all_meaning = html.find_all("div", {"class": "synonyms-list-group"})

meaning_index = 0
word_index = 0
more_synonym = True
while(more_synonym):
    try:
        # filter the ad
        if all_meaning[meaning_index].text.strip() == "Anzeige":
            meaning_index += 1
        print('\033[94m' + all_meaning[meaning_index].text.strip() + '\033[0m')
        list_of_words = all_synonyms[word_index].text.split("\n")
        for word in list_of_words[1:5]:
            sys.stdout.write(word + " : ")
        print("\n \n")
        ans = raw_input('\033[93m More synonyms? (Y/n) \033[0m << ').lower()
        if ans in ['yes', 'y', '']:
            more_synonym = True
        elif ans in ['no', 'n']:
            more_synonym = False
        else:
            more_synonym = False
            print(" \033[31minvalid input. Close script.")
        meaning_index += 1
        word_index += 1
        print("")
    except IndexError:
        print("No more synonyms.")
        exit()
