from animal import Animal


class Mammal(Animal):
    def __init__(self, species, name, age, gender, num_legs):
        super().__init__(species, name, age, gender)
        self.num_legs = num_legs

    def nurse(self):
        print(f"{self.species} is nursing its young")

    def give_birth(self):
        print(f"{self.name} is giving birth")

    def make_sound(self):
        print(f"{self.name} makes a sound when scared")

