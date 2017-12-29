import urllib2

response = urllib2.urlopen('http://dobreprogramy.pl')
html = response.read()
with open('page.html', 'w') as writer:
    writer.write(html)
