def getNumbers():
    list = []
    size = input('Podaj ilosc liczb: ')
    index = 0
    while index < size:
        list.append(raw_input('Podaj liczbe: '))
        index += 1
    return list

numbers = getNumbers()
print 'Podaj kierunek sortowania:'
print '1.Rosnaco'
print '2.Malejaco'
option = input("Wybierz: ")
if option == 1:
    numbers.sort()
else:
    numbers.sort(reverse=True)

print numbers
