size = input('Podaj ilosc elementow ciagu Fibonacciego: ')


def fib(size):
    return [int(((1.6180339887 ** x) / 2.2460679775)) for x in range(1, size)]


print fib(size)
