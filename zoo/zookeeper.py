class Zookeeper:
    def __init__(self, name, age, animals=[]):
        self.name = name
        self.age = age
        self.animals = animals

    def feed_animals(self):
        for animal in self.animals:
            print("{} is feeding {}".format(self.name, animal.species))

    def clean_habitats(self):
        for animal in self.animals:
            print("{} is cleaning {}".format(self.name, animal.species))
