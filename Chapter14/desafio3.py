class Square:
    def __init__(self, sides):
        self.sides = sides

def true_or_false(x, y):
    if x is y:
        print('True')
    else:
        print('False')

square = Square(5)
same_square = square
another_square = Square(10)

print(true_or_false(square, same_square))
print(true_or_false(square, another_square))