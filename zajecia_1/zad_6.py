size = input('Podaj ile liczb ciagi Fibonacciego chcesz zobaczyc: ')
first = 0
second = 1
temp = 1
index = 0

while index < size:
    temp = second
    second = first + second
    first = temp
    print second
    index += 1

