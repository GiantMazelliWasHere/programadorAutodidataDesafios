'''

Retorna o float da string
param str: numero
return: O numero escrito na string em forma de float

'''

def str_to_float(str):
    return float(str)

try:
    print(str_to_float(input('Give me a number: ')))

except ValueError:
    print('The input is not valid!')