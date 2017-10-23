import math


def distance(point1, point2):
    return math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2))


def fun(points, pointControl):
    distance(pointControl, pointControl)
    pointsWithDistance = [(distance(pointControl, point), point) for point in points]
    return sorted(pointsWithDistance, key=lambda point: pointsWithDistance[0])


print distance((1, 1), (2, 1))
print fun([(2, 3), (5, 5), (4, 10), (1, 1), (1, 1)], (1, 2))
