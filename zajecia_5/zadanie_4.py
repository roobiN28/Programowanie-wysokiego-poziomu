import re
pesel = r'95082308171'
regexPESEL = re.compile(r'''(?P<PESEL>\d+
)''')
ma= regexPESEL.match(pesel)
ma.groupdict()