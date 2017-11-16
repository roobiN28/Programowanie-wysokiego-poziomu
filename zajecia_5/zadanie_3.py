import re

regex_ip = re.compile(r'^(?P<addresss_ip>'
                      r'(?P<first>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
                      r'.'
                      r'(?P<second>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
                      r'.'
                      r'(?P<third>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
                      r'.'
                      r'(?P<fourth>25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
                      r')$')
with open('zadanie_3_file.txt') as file:
    for line in file:
        regex = regex_ip.match(line)
        if regex:
            print regex.groupdict()
