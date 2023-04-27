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
order1 = Order(1)
order1.add_item(appetizer1)
order1.add_item(entree1)
order1.add_item(drink1)

# Create another order
crackers = Appetizer("Crackers", 15.50, "Cheddar Cracker Appetizer Bites", True, False)
butter_chicken = Entree("Butter chicken", 100.10, "Grilled chicken in a luscious tomato-based spiced curry sauce", False, False)
tea = Drink("Tea", 12.30, "Different in the assortement", "Large", False)
order2 = Order(2)
order2.add_item(appetizer2)
order2.add_item(entree2)
order2.add_item(drink2)

# Create a restaurant
my_restaurant = Restaurant("Family Food")
my_restaurant.add_order(1, order1)
my_restaurant.add_order(2, order2)

# Print the orders in the restaurant
orders = my_restaurant.get_orders()
for table_number, order in orders.items():
    print(f"Table {table_number}: {[item.get_name() for item in order.get_items()]} - Total: ${order.get_total()}")
