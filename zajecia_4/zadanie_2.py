
def createDictionary(filename):
    dics = {}
    with open(filename) as file:
        for line in file:
            splitted = line.strip().split(':')
            dics[splitted[0]] = splitted[1]
    return dics

print createDictionary('zadanie_2_file.txt')
