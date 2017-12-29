import urllib2
from xml.dom import minidom


def getValue(node):
    return node[0].childNodes[0].nodeValue

city = raw_input('Podaj miejscowosc: ')
rss = 'http://www.yr.no/place/Poland/'+city+'/'+city+'/forecast.xml'
response = urllib2.urlopen(rss)
weather = response.read()
dom = minidom.parseString(weather)
sun = dom.getElementsByTagName('sun')
print 'Godzina wschodu Slonca dla ' + city + ' to: ' + sun[0].getAttribute('rise')[11:]