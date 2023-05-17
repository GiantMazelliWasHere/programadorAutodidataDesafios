class Square:
    square_list = []

    def __init__(self, sides):
        self.sides = sides
        self.square_list.append(self.sides)

    def __repr__(self):
        return f'{self.sides} by {self.sides}'

# Desafio 1 #
#s1 = Square(5)
#s2 = Square(10)
#s3 = Square(15)
#s4 = Square(20)
#s5 = Square(25)

#print(Square.square_list)

# Desafio 2 #
square = Square(25)

print(square)