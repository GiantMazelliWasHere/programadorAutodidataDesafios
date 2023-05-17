class Apple:
    def __init__(self, h, w, t, f):
        self.height = h
        self.width = w
        self.taste = t
        self.freshness = f

apple = Apple(5, 2.5 , 'Sweet', 'Fresh')

print(f'{apple.height} {apple.width} {apple.taste} {apple.freshness}')