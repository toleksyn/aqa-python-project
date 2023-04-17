
from animal import Animal

class Reptile(Animal):
    def __init__(self, species, name, age, genger, scale_color):
        super().__init__(species, name, age, genger)
        self.scale_color = scale_color

    def bask(self):
        print(f"{self.name} is basking in the sun.")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")