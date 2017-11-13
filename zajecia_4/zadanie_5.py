import sys

def encode(input):
    encoded = ''
    for char in list(input):
        ascii = (ord(char))
        if ascii == 32:
            encodedAscii = 32
        elif ascii >= 120:
            encodedAscii = ascii - 22
        elif 88 <= ascii <= 90:
            encodedAscii = ascii - 22
        else:
            encodedAscii = ascii + 3
        encoded += unichr(encodedAscii)
    return encoded


with open(sys.argv[1]) as reader:
    writer = open(sys.argv[2], 'w')
    for line in reader:
        writer.write(encode(line.strip()))
        writer.write('\n')
