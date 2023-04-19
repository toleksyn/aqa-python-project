from mammal import Mammal
giraffe = Mammal("Giraffe", "Lola", 3, "Female", 4)

from bird import Bird
owl = Bird("Owl", "Lu", 3, "Female", 2)

from reptile import Reptile
crocodile = Reptile("Crocodile", "Milo", 5, "Male", "Green")

from zookeeper import Zookeeper
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
