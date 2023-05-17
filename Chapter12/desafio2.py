import math

class Circle:
    def __init__(self, d):
        self.d = d
        self.r = d / 2
    
    def area(self):
        return math.pi * (self.r ** 2)

circle = Circle(5)

print(circle.area())