def createDictionary(string):
    dics = {}
    for pair in string.splitlines():
        splitted = pair.split(':')
        dics[splitted[0]] = splitted[1]
    return dics

print createDictionary('k1:w1\nk2:w2\nk3:w3')
