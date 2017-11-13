import sys


class Reader(object):
    def __init__(self, func=None):
        if func:
            self.read = func


def readFromFile(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [(line.strip()) for line in lines]


def readFromKeyboard():
    lines = []
    print 'Wpisz znaki. Na koncu nacisnij enter'
    line = raw_input()
    while line:
        lines.append(line)
        line = raw_input()
    return lines

############### main ######################
if sys.argv[1] is '-':
    print 'key'
    reader = Reader(readFromKeyboard)
else:
    print sys.argv[1]
    reader = Reader(lambda: readFromFile(sys.argv[1]))

lines = reader.read()
for line in lines:
    if sys.argv[2] in line:
        print line