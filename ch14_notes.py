print('=================== Our first Python class ===========================')

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
print('==============================================')

an = PartyAnimal()
print("Type", type(an))
print("Dir ", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))

print('=================== Object lifecycle ===========================')


class PartyAnimal_2:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


an = PartyAnimal_2()
an.party()
an.party()
an = 42
print('an contains', an)

print('==================== Multiple instances ==========================')


class PartyAnimal_3:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


s = PartyAnimal_3('Sally')
j = PartyAnimal_3('Jim')

s.party()
j.party()
s.party()

print('===================== Inheritance =========================')

# from party import PartyAnimal

class CricketFan(PartyAnimal_3):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal_3("Sally")
s.party()
j = CricketFan("Jim")
j.party()
print(' >>> quick pause before j.six()')
j.six()
print(dir(j))

