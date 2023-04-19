from animal import Animal

class Bird(Animal):
    def __init__(self, species, name, age, gender, wingspan):
        super().__init__(species, name, age, gender)
        self.wingspan = wingspan

    def eat(self):
        print("{} is eating.".format(self.name))

    def sleep(self):
        print("{} is sleeping.".format(self.name))

    def make_sound(self):
        print("{} is making sound.".format(self.name))

    def fly(self):
        print("The {} is flying.".format(self.species))

    def lay_eggs(self):
        print("The {} is laying eggs.".format(self.species))
