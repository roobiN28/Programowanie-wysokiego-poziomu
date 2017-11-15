import re

s = '111.111.111.1111' \
    '22.22.22.2'
regexIP = re.compile(r'^' +
                     r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.' +
                     r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.' +
                     r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.' +
                     r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])'
                     )
regexIP = re.compile(r'(?P<adres>(' +
                     r'?P<first>(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.' +
                     r'?P<second>(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.' +
                     r'?P<second>(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.' +
                     r'?P<second>(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))'
                     )
# for match_string in regexIP.finditer(tekst):
#     print match_string.groupdict()

with open('zadanie_3_file.txt') as file:
    for line in file:
        address = line.strip()
        regex = regexIP.findall(address)
        print regex
        #
        #
        # for line in file:
        #     add
        #     print ip_candidates.groupdict()
with open('zadanie_3_file.txt') as file:
    ips = ' '.join(file.readlines()).replace('\n', ' , ')
    print ips
    for match_string in regexIP.finditer(ips):
        print match_string