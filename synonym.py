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

#print(html)

all_synonyms = html.find_all("div", {"class": "upper-synonyms"})
first_meaning = html.find_all("div", {"class": "synonyms-list-group first"})
all_meaning = html.find_all("div", {"class": "synonyms-list-group"})

# main meaning
print('\033[94m' + first_meaning[0].text.strip() + '\033[0m')
first_synonyms = all_synonyms[0]
list_of_words = first_synonyms.text.split("\n")
for word in list_of_words[1:5]:
    sys.stdout.write(word + " : ")
print("\n \n")

try:
  ans = raw_input('\033[93m More synonyms? (Y/n) \033[0m << ')[0].lower()
except:
  ans = ''
if ans in ['yes', 'y', '']:
    more_synonym = True
elif ans in ['no', 'n']:
    more_synonym = False
else:
    more_synonym = False
    print("\033[31minvalid input. Close script.")

print("\n \n")

meaning_index = 1
word_index = 1
while(more_synonym):
    try:
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
#table_types = mensa_html.find_all("td", {"class": "mensatype"})

#table_food = mensa_html.find_all("table", {"class": "easy-tab-dot"})

#column = []

# regex = (\d+\,\d{1,2})
'''for i, l in enumerate(table_types[0:6]):
    tables = []
    tables.append(str(l.text))
    for lines in table_food[i]:
        for k, child in enumerate(lines.children):
            if k == 0 or k == 2:
                continue
            rest = child.text.split('[', 1)[0]
            tables.append(str(rest))
    column.append(tables)

for columns in column:
    print columns[0]
    print '----------'
    for food in columns[1:]:
        print food
    print '\n'
'''
