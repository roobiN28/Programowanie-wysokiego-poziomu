def getAlphabet(step):
    index = 0
    alphabet = ''
    while index < 26:
        if index % 2:
            alphabet += unichr(index + 65)
        else:
            alphabet += unichr(index + 97)
        index += step
    return alphabet

step = input('Podaj co ktora litere z alfabetu wyswietlic: ')
print getAlphabet(step)
