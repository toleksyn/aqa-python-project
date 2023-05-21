from mammal import Mammal
from bird import Bird
from reptile import Reptile
from zookeeper import Zookeeper

giraffe = Mammal("Giraffe", "Lola", 3, "Female", 4)

owl = Bird("Owl", "Lu", 3, "Female", 2)

crocodile = Reptile("Crocodile", "Milo", 5, "Male", "Green")

zookeeper_one = Zookeeper("Emma", 27, [giraffe, owl, crocodile])
zookeeper_two = Zookeeper("Tom", 30, [giraffe, owl, crocodile])
zookeeper_one.feed_animals()
zookeeper_two.clean_habitats()

giraffe.nurse()
giraffe.make_sound()
owl.fly()
owl.sleep()
crocodile.bask()
crocodile.eat()
