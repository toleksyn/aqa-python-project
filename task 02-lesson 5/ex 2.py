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


class Mammal(Animal):
    def __init__(self, species, name, age, gender, num_legs):
        super().__init__(species, name, age, gender)
        self.num_legs = num_legs

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")

    def nurse(self):
        print(f"The {self.species} is nursing its young.")

    def give_birth(self):
        print(f"The {self.species} is giving birth to its young.")



class Zookeeper:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.responsible_animals = []

    def add_animal(self, animal):
        self.responsible_animals.append(animal)

    def feed_animals(self):
        print(f"{self.name} is feeding the animals.")
        for animal in self.responsible_animals:
            animal.eat()

    def clean_habitats(self):
        print(f"{self.name} is cleaning the habitats.")
        for animal in self.responsible_animals:
            print(f"{self.name} is cleaning {animal.name}'s habitat.'")

lion = Mammal("lion", "Simba", 10, "male", 4)
giraffe = Mammal("giraffe", "Geoffrey", 5, "male", 4)

zookeeper = Zookeeper("Jane", 30)
zookeeper.add_animal(lion)
zookeeper.add_animal(giraffe)

zookeeper.feed_animals()
zookeeper.clean_habitats()
