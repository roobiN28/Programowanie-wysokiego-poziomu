def fibonacciGenerator():
    p = 1
    n = 2
    yield p
    yield n
    while True:
        t = n + p
        p = n
        n = t
        yield n

fibonacci = fibonacciGenerator()

print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
print fibonacci.next()
