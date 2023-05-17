class Square:
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return 4 * self.side
    
    def change_size(self, change):
        return self.side + change
        
square = Square(10)

print(square.change_size(5))
print(square.change_size(-5))
print(square.change_size(0))