'''

Retorna o quadrado do numero
param number: int
return: quadrado do number

'''
def square_root(number):
    n = int(number)

    return n ** 2

r = square_root(input('What number you want the square root of: '))

print(r)