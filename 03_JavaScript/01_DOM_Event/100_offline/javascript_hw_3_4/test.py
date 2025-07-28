class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangular:
    def __init__(self, pos_1, pos_2):
        self.pos_1 = pos_1
        self.pos_2 = pos_2

p1 = Point(0, 0)
p2 = Point(2, 2)

r1 = Rectangular(p1, p2)

print(r1.pos_1.x)