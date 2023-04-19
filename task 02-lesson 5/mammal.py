from animal import Animal

class Mammal(Animal):
    def __init__(self, species, name, age, gender, num_legs):
        super().__init__(species, name, age, gender)
        self.num_legs = num_legs

    def eat(self):
        print("{} is eating.".format(self.name))

    def sleep(self):
        print("{} is sleeping.".format(self.name))

    def make_sound(self):
        print("{} is making sound.".format(self.name))

    def nurse(self):
        print("The {} is nursing its young.".format(self.species))

    def give_birth(self):
        print("The {} is giving birth.".format(self.species))
