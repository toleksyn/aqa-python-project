from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species, name, age, gender):
        self.species = species
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass
