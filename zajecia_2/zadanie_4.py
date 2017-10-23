def isEven(number):
    return number % 2 == 0


def listPredicate(fun, list):
    return [i for i in list if fun(i)]

def pierwsze(n):
    return [i for i in range(2, n) if len([t for t in range(1, i+1) if i % t == 0]) == 2]

print listPredicate(isEven, range(0, 50))
print pierwsze(10)
