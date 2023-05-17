class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        print('I am a Shape')


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return 4 * self.side
    
class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.base + self.height)
    
square = Square(5)
rectangle = Rectangle(10,5)

print(square.what_am_i())
print(rectangle.what_am_i())