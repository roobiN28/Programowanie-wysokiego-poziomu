def getAlphabet():
    index = 0
    alphabet = ''
    while index < 26:
        if index % 2:
            alphabet += unichr(index + 65)
        else:
            alphabet += unichr(index + 97)
        index += 1
    return alphabet

print getAlphabet()
