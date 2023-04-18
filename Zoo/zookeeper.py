# 5. Zookeeper - This class should have the following attributes: name, age, and list of animals they
# are responsible for. It should also have the following methods: feed_animals() and clean_habitats()
class Zookeeper:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_of_animals = []

    def feed_animals(self, animal):
        print("I'm feeding", animal.name)

    def clean_habitats(self, animal):
        print("I'm cleaning", animal.name)

    def add_animal(self, animal):
        self.list_of_animals.append(animal)

    def animals_responsibility(self, animal):
        print("My name is", self.name, "I'm", self.age, "years old! I'm responsible for:", len(self.list_of_animals),
              "animals")
        for animal in self.list_of_animals:
            print(animal.species, "called", animal.name)

