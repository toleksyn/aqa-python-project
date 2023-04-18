# 2. Mammal - This class should inherit from the Animal class and have the additional attribute of number of legs.
# It should also have the following methods: nurse() and give_birth().
from Zoo.animal import Animal


class Mammal(Animal):

    def __init__(self, species, name, age, gender, number_of_legs):
        super().__init__(species, name, age, gender)
        self.number_of_legs = number_of_legs

    def nurse(self):
        print("I can nurse my baby!")

    def give_birth(self):
        print("I can give birth to new animal!")

    def make_sound(self):
        print("I can make a sound via mouth!")
