def encode(input):
    encoded = ''
    for char in list(input):
        encoded += unichr((ord(char) + 3))
    return encoded

data = raw_input('Podaj ciag znakow do zaszyfrowania: ')
print encode(data)
