from restaurant import Restaurant
from appetizer import Appetizer
from entree import Entree
from drink import Drink
from menu_item import MenuItem
from order import Order

# Create a restaurant
restaurant = Restaurant("Faro del Porto")

# Create menu items
tofu = Appetizer("Spicy Tofu", 5.99, "Crispy tofu bites with a spicy dipping sauce", True, True)
chicken = Entree("Grilled Chicken", 15.49, "Juicy grilled chicken breast with steamed vegetables", False, True)
soda = Drink("Soda", 2.50, "Refreshing soda", "Large", True)
tonic = Drink("Tonic", 2.99, "Classic tonic", "Medium", True)
burger = MenuItem("Burger", 9.99, "Juicy beef patty on a sesame seed bun", False)
fries = MenuItem("Fries", 3.99, "Crispy golden fries", True)

# Create orders
first_order = Order(1) # Table number is 1
first_order.add_item(tofu)
first_order.add_item(chicken)
first_order.add_item(soda)
print(first_order)

second_order = Order(2) # Table number is 2
second_order.add_item(tofu)
second_order.add_item(fries)
second_order.add_item(tonic)
print(second_order)
