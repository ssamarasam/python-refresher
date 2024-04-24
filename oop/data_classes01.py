from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
print(Point)
print(type(Point))

p1 = Point(x=1, y=2)
p2 = Point(x=3, y=8)
p3 = Point(x=1, y=2)
print(p1 == p2)
print(p1 == p3)
