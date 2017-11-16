import re
pesel = r'91221141171'
regexPESEL = re.compile(r'^(?P<pesel>'
                        r'(?P<year>\d\d)'
                        r'(?P<month>\d\d)'
                        r'(?P<day>\d\d)'
                        r'\d\d\d'
                        r'(?P<sex>\d)'
                        r'\d'
                        r')$')

match = regexPESEL.match(pesel)
if int(match.group('sex')) % 2:
    sex = 'Mezczyzna'
else:
    sex = 'Kobieta'
print 'Birthdate: 19' + match.group('year') + '-' +\
      match.group('month') + '-' + \
      match.group('day') + \
      ', sex: ' + sex
