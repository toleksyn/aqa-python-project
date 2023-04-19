from mammal import Mammal
from bird import Bird
from reptile import Reptile
from zookeeper import Zookeeper

mammal = Mammal("Bear", "Balu", 10, "Female", 4)
bird = Bird("Tucan", "Rembo", 5, "Male", 30)
reptile = Reptile("Crocodile ", "Sebek", 50, "Male", "Green")
zookeeper = Zookeeper("Bob", 30, "responsible for: mammal, bird, reptile")


print(mammal.__dict__)
mammal.nurse()
mammal.give_birth()
print(bird.__dict__)
bird.fly()
bird.lay_eggs()
print(reptile.__dict__)
reptile.bask()
reptile.lay_eggs()
zookeeper.list_of_animals()
zookeeper.feed_animals()
zookeeper.clean_habitats()
