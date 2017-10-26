# klasy

class Klasa:
    def function(self):
        print 'metoda'
        self.variable = 5
        print self.variable

    def function2(self, number):
        self.function()
        print number


obiekt = Klasa()
obiekt.function2(100)


class Klasa2:
    atrr1 = None
    __attr2 = None

    def setAttr2(self, zmienna):
        self.__attr2 = zmienna

    def setAttr3(self, zmienna):
        self.attr3 = zmienna

    def add(self):
        return self.attr1 + self.__attr2 + self.attr3


obiekt = Klasa2()
obiekt.attr1 = 4
obiekt.setAttr2(5)
obiekt.setAttr3(10)
print obiekt.add()

obiekt.__attr2 = 100


# dziedziczenie

class Car(object):
    color = None

    def setColor(self, color):
        self.color = color


class PersonalCar(Car):
    brand = 'Mercedes'

    def setBrandAndColor(self, brand, color):
        self.brand = brand
        super(PersonalCar, self).setColor(color)


car = PersonalCar()
car.setBrandAndColor('Audi', 'niebieski')
print car.color + '   ' + car.brand


class A:
    def __init__(self, zmienna):
        self.zmienna = zmienna

    def __add__(self, other):
        return self.zmienna + other.zmienna


print A(5) + A(10)
