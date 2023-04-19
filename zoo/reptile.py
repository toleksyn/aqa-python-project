from animal import Animal


class Reptile(Animal):
    def __init__(self, species, name, age, gender, scale_color):
        super().__init__(species, name, age, gender)
        self.scale_color = scale_color

    def bask(self):
        print(f"{self.species} is basking in the sun")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs")

    def eat(self):
        print(f"{self.name} eats a lot of meat")
