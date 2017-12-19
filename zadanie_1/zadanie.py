# coding=utf-8
import urllib2
import re
from bs4 import BeautifulSoup
from collections import defaultdict


def removeScripts(soup):
    [s.extract() for s in soup('script')]


def removeShorter(words, minimum=4):
    newList = []
    for word in words:
        if len(word) >= minimum:
            newList.append(word)
    return newList


def top(words):
    counts = defaultdict(int)
    for word in words:
        counts[word] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:5]


with open('lista_stron') as file:
    most = []
    for pageAddress in file:
        response = urllib2.urlopen('http://' + pageAddress)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        removeScripts(soup)

        text = soup.text
        words = re.sub(u"[^\wążźćęńłóĄŻŹĘŃÓŁ]", " ", text, re.UNICODE).split()

        words = removeShorter(words)
        most.append((pageAddress, top(words)))

    search = raw_input("Podaj szukane słowo: ")
    findedOn = ''
    for page in most:
        for tuple in page[1]:
            if tuple[0].encode('utf-8') == search:
                findedOn += page[0] + ', '

    if findedOn == '':
        print 'Nie znaleziono słowa na stronach'
    else:
        print "Słowo znalezione na stronie: " + findedOn[:-2]
