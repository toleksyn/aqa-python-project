# 4. Reptile - This class should also inherit from the Animal class and have the additional attribute of scale color.
# It should also have the following methods: bask() and lay_eggs().
from Zoo.animal import Animal


class Reptile(Animal):

    def __init__(self, species, name, age, gender, scale_color):
        super().__init__(species, name, age, gender)
        self.scale_color = scale_color

    def bask(self):
        print("I can bask on a sun!")

    def lay_eggs(self):
        print("I can lay eggs!")

    def make_sound(self):
        print("I can only hiss!")