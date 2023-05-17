'''

Retorna a string com os dados passados aos parametros
param name: str
param age: int
param type: str
param year: int
param month: str
return: A string passada para a função, formatada com os parametros

'''

def my_type(name, age, type, year = 2023, month = 'april'):
    print(f"Hi my name is {name}, I'm {age} and I like {type}. Today is {month} of {year}")

n = input("What's your name? ")
a = input("How old are you? ")
t = input("What is your type of man/woman? ")

types = my_type(n,a,t)

print(types)