import sys


def createWordCounterDictionary(words):
    words.sort()
    dics = {}
    counter = 1
    last = words.pop()
    for word in words:
        if last != word:
            dics[last] = counter
            counter = 1
            last = word
        else:
            counter += 1
    dics[last] = counter
    return dics

with open(sys.argv[1]) as file:
    dics = createWordCounterDictionary(file.read().split())
    print dics
