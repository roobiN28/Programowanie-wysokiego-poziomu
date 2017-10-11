# zmienne
# data = raw_input("Wprowadz dane:") #zawsze string, lepiej z tego raczej korzystac
# data = input("Wprowadz dane:") #python sam ustala typ
# print data

L1 = 3
L2 = 4.5
L3 = '6'

print (L1)
print (L2)
print (L3)
print (L1 + L2)
print (L1 + int(L3))


# funkcje
def suma(a, b):
    return a + b


print suma(2, 10)
print suma('a', 'b')

# if else
a = 2
b = 4

if (a > b):
    print('Wieksze')
elif (a == b):
    print('Mniejsze')
else:
    print('Mniejsze')

# petle
i = 0
while (i < 5):
    print 'Iteracja while:' + str(i)
    i += 1

    # tu for

# listy
li = [1, 2, 3, 4, 5, 'x']
print li
li[2] = 'Nowa wartosc'
print li

# krotki
kr = (2, 3, 4, 'y')
print kr
