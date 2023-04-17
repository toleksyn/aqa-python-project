
from mammal import Mammal
from bird import  Bird
from reptile import Reptile
from zookeeper import Zookeeper

# Create some animals
dog = Mammal("Labrador", "Kora", 2, "F", 4)
owl = Bird("Snowy Owl", "Hedwig", 5, "M", 77)
snake = Reptile("Salazar's pit viper", "Nagini", "F", 10, "dark green")

# Create a zookeeper responsible for these animals
zookeeper = Zookeeper("Hagrid", 40, [dog, owl, snake])

# Interact with the animals via the zookeeper
dog.nurse()
dog.give_birth()
dog.eat()
dog.sleep()
dog.make_sound()
owl.fly()
owl.lay_eggs()
owl.eat()
owl.sleep()
owl.make_sound()
snake.bask()
snake.lay_eggs()
snake.eat()
snake.sleep()
snake.make_sound()
zookeeper.feed_animals()
zookeeper.clean_habitats()