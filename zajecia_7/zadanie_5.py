def getWord():
    with open('text.txt') as file:
        text = ''.join(file.readlines()).replace('\n', ' ')

        for word in text.split(' '):
            yield (word, len(word))

for word in getWord():
    print 'Slowo ' + word[0] + ' ma dlugosc:' + str(word[1])