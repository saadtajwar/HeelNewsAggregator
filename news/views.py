from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Scraping news heads from DTH Campus section

toi_r = requests.get("https://www.dailytarheel.com/section/campus")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

# Taking all of the headings labeled h2 in HTML (which is what all the headlines are under)
toi_headings = toi_soup.find_all('h2')


# toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from WRAL UNC section

ht_r = requests.get("https://www.wral.com/unc/17382381/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "featured_text"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})
