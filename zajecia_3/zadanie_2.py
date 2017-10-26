import math


class Point2D(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))


class Point3D(Point2D):
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        return math.sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2) + pow(other.z - self.z, 2))


a = Point2D(1, 1)
b = Point2D(1, 2)

print a.distance(b)

c = Point3D(1, 2, 3)
d = Point3D(2, 3, 4)
print c.distance(d)
