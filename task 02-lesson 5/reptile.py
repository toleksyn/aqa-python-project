from animal import Animal

class Reptile(Animal):
    def __init__(self, species, name, age, gender, scale_color):
        super().__init__(species, name, age, gender)
        self.scale_color = scale_color

    def eat(self):
        print("{} is eating.".format(self.name))

    def sleep(self):
        print("{} is sleeping.".format(self.name))

    def make_sound(self):
        print("{}is making sound.".format(self.name))

    def bask(self):
        print("The {}is basking in the sun.".format(self.species))

    def lay_eggs(self):
        print("The {}is laying eggs.".format(self.species))
