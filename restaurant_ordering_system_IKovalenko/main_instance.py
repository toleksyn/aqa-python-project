from appetizer import Appetizer
from entree import Entree
from drink import Drink
from order import Order
from restaurant import Restaurant

# Create some menu items
mussels = Appetizer("Mussels", 9.99, "Mussels In Lemon Garlic-Butter Sauce", True, True)
borscht = Entree("Borscht", 49.95, "Traditional Ukrainian Borscht", False, True)
juice = Drink("Juice", 12.30, "Natural juices in the assortement", "Medium", True)

# Create an order
first_order = Order(1)
first_order.add_item(mussels)
first_order.add_item(borscht)
first_order.add_item(juice)

# Create another order
crackers = Appetizer("Crackers", 15.50, "Cheddar Cracker Appetizer Bites", True, False)
butter_chicken = Entree("Butter chicken", 100.10, "Grilled chicken in a luscious tomato-based spiced curry sauce", False, False)
tea = Drink("Tea", 12.30, "Different in the assortement", "Large", False)
second_order = Order(2)
second_order.add_item(crackers)
second_order.add_item(butter_chicken)
second_order.add_item(tea)

# Create a restaurant
my_restaurant = Restaurant("Family Food")
my_restaurant.add_order(1, first_order)
my_restaurant.add_order(2, second_order)

# Print the orders in the restaurant
my_restaurant.print_orders(1)
my_restaurant.print_orders(2)
