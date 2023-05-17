import desafio3

def atributte(info):
    return desafio3.atributos[info]

q = input('What info you want to know? ')

if q == 'eyes':
    print(atributte('eyes'))
elif q == 'hair':
    print(atributte('hair'))
elif q == 'height':
    print(atributte('height'))
elif q == 'favourite color':
    print(atributte('favourite color'))
elif q == 'favourite actor':
    print(atributte('favourite actor'))
else:
    print('Top Secret Information!!')
