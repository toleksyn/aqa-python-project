from animal import Animal


class Bird(Animal):
    def __init__(self, species, name, age, gender, wingspan):
        super().__init__(species, name, age, gender)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.species} flies at night")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs")

    def sleep(self):
        print(f"{self.name} sleeps all day")
