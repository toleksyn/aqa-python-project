class Zookeeper:
    def __init__(self, name, age, animals_responsible_for):
        self.name = name
        self.age = age
        self.animals_responsible_for = animals_responsible_for

    def feed_animals(self):
        print("The zookeeper is feeding the animals.")

    def clean_habitats(self):
        print("The zookeeper is cleaning the habitats.")

    def list_of_animals(self):
        print('Zookeeper Bob is responsible for Bear, Tucan, Crocodile')