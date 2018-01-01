import math


def splitNumber(number):
    splits = []
    g = math.sqrt(number)
    i = 2

    while i <= g:
        while number % i == 0:
            splits.append(i)
            number /= i
        if number == 1:
            return splits
        splits.append(number)
        i += 1
    return splits


def createPairs(splits):
    last = -1
    counter = 0
    ret = []
    for split in splits:
        if last != split:
            if counter != 0:
                ret.append((last, counter))
                counter = 0
            last = split
            counter = 1
        else:
            counter += 1
    ret.append((last, counter))
    return ret


splits = splitNumber(200)
splits.sort()
print createPairs(splits)
