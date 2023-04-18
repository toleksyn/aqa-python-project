# 1. Animal - This class should be abstract and have the following attributes: species, name, age, and gender.
# It should also have the following methods: eat(), sleep(), and make_sound().
from abc import abstractmethod


class Animal:

    def __init__(self, species, name, age, gender):
        self.species = species
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")

    @abstractmethod
    def make_sound(self):
        pass
