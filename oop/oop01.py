class Point:
    # class variable
    default_color = "yellow"

    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y} )"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(type(point))
print(isinstance(point, Point))
point.draw()
print(Point.default_color)
print(point.default_color)
Point.default_color = "red"
print(Point.default_color)
print(point.default_color)
another = Point.zero()
print(another)
another.draw()
print(another)

point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(5, 7)
print(point1 == point2)
print(point3 > point1)
combined = point1 + point3
print(combined)
