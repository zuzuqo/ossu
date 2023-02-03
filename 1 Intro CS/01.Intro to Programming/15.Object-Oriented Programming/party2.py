class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print(f'So far, {self.x}')

an = PartyAnimal()
bb = PartyAnimal()

an.party()
an.party()
an.party()

PartyAnimal.party(an)
PartyAnimal.party(bb)
