def makeTuple(sentence):
    return [(word, len(word)) for word in sentence.split()]

print makeTuple('Ala ma kota a kot nie ma Ali')