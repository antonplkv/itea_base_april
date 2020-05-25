class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __eq__(self, other):
        return all([self.x == other.x, self.y == other.y])

    def __add__(self, other):
        return self.x + other.x, self.y + other.y


a = Point(11, 20)
b = Point(10, 20)

print(isinstance(a, Point))
print(a == b)

r = a + b
print(r)