class Rider:
    def __init__(self, name):
        self.name = name

class Horse:
    def __init__(self,name, owner):
        self.name = name
        self.owner = owner

michael = Rider('Michael')
bojack = Horse('BoJack', michael)

print(michael.name)
print(bojack.name)
print(bojack.owner.name)