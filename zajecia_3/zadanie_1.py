import math


class Complex(object):
    x = 0
    y = 0

    def __init__(self, real, complex):
        self.x = real
        self.y = complex

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y,
                       self.x * other.y + self.y * other.x)

    def __div__(self, other):
        return Complex((self.x * self.y + other.x * other.y) / (pow(self.x, 2) + pow(other.y, 2)),
                       (other.x * self.y - self.x * other.y) / (pow(self.x, 2) + pow(other.y, 2)))

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + 'i'

    def modul(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __cmp__(self, other):
        return self.modul() > other.modul()


a = Complex(1, 2)
b = Complex(1, 4)

print a + b
print a - b
print a * b
print a / b
print a.modul()
print b.modul()
print a < b
