#listy skladane
liczby = range(0, 20)
kwadraty = [(x, x ** 2) for x in liczby]
print kwadraty


#funkcje wyzszego rzedu
def fun1(a):
    def fun2(b):
        return a - b
    return fun2

def fun3(c):
    print c(11)


res = fun1(5)
print res(10)

fun3(res)

#wyrazenia lambda
kwadrat = lambda y: y*y
print kwadrat(2)


#generator
def generator(n):
    while n:
        print 'Generator start %d' % n
        yield n
        print 'Generator stop %d' % n
        n -= 1

for a in generator(5):
    print 'Wywolnie %d' % a


gen = generator(5)
print gen.next()
print gen.next()