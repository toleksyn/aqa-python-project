# 3. Bird - This class should also inherit from the Animal class and have the additional attribute of wingspan.
# It should also have the following methods: fly() and lay_eggs().
from Zoo.animal import Animal


class Bird(Animal):

    def __init__(self, species, name, age, gender, wingspan):
        super().__init__(species, name, age, gender)
        self.wingspan = wingspan

    def fly(self):
        print("I can fly!")

    def lay_eggs(self):
        print("I can lay eggs!")

    def make_sound(self):
        print("I can make a sound via beak!")