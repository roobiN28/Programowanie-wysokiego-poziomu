import urllib2
from xml.dom import minidom


def getValue(node):
    return node[0].childNodes[0].nodeValue


rss = 'https://www.gry-online.pl/rss/news.xml'
response = urllib2.urlopen(rss)
feed = response.read()
dom = minidom.parseString(feed)
items = dom.getElementsByTagName('item')
counter = 1
for item in items:
    title = item.getElementsByTagName('title')
    link = item.getElementsByTagName('link')
    description = item.getElementsByTagName('description')

    print 'Artykul numer: ' + str(counter)
    print getValue(title)
    print 'Link: ' + getValue(link)
    print 'Opis: ' + getValue(description)
    counter += 1
