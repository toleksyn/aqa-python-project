
from animal import Animal

class Bird(Animal):
    def __init__(self, species, name, age, genger, wingspan):
        super().__init__(species, name, age, genger)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying.")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")