#!/usr/bin/env python
# -*- coding: utf-8 -*-

napisUnicode = u'Zażółć gęślą jaźń'
napisStr = napisUnicode.encode('utf8')
napisUnicode2 = napisStr.decode('utf8')
print napisUnicode
print napisStr
print napisUnicode2
print len(napisUnicode)
print len(napisStr)
print isinstance(napisStr, basestring)

test = 'TEST'
print test.center(30)
print test.capitalize()
print test.lower().islower()
print test.startswith('TE')
# wyrazenia regularne
import re

regex_email = re.compile(r'(?P<adres>(?P<login>[\w+.]+)@(?P<domena>[\w+.\w+]+))', re.IGNORECASE | re.VERBOSE)

tekst = u'"mail1@poczta.pl", "jan.nowak@wp.eu"'

for match_string in regex_email.finditer(tekst):
    print match_string.groupdict()

#Serializacja obiektów
#JSON
print 'JSON'.center(50, '-')
import json
slownik = {
    'k1':'w1'
}

jsonStr = json.dumps(slownik)
print jsonStr
print json.loads(jsonStr)

#PICLE
print 'PICLE'.center(50, '-')
import pickle

pickleStr = pickle.dumps(slownik)
print pickle.loads(pickleStr)
