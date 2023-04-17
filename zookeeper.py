
class Zookeeper:
    def __init__(self, name, age, responsible_animals):
        self.name = name
        self.age = age
        self.responsible_animals = responsible_animals

    def feed_animals(self):
        for animal in self.responsible_animals:
            print(f"{self.name} is feeding {animal.name} the {animal.species}.")

    def clean_habitats(self):
        for animal in self.responsible_animals:
            print(f"{self.name} is cleaning {animal.name}'s habitat.")