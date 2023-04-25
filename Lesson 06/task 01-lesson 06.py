from appetizer import Appetizer
from drink import Drink
from entree import Entree
from order import Order
from restaurant import Restaurant

restaurant = Restaurant("Cherkasy")

order1 = Order(1)
order1.add_item(Appetizer("Spring Rolls", 5.99, "Crispy vegetarian spring rolls", True, False))
order1.add_item(Entree("Pad Thai", 11.99, "Rice noodles stir-fried with vegetables and peanuts", True, True))
order1.add_item(Drink("Thai Iced Tea", 2.99, "Sweetened Thai tea", "Large", False))

order2 = Order(2)
order2.add_item(Appetizer("Fried Calamari", 8.99, "Crispy calamari rings with marinara sauce", False, True))
order2.add_item(Entree("Grilled Salmon", 16.99, "Freshly grilled salmon with lemon herb butter sauce", False, True))
order2.add_item(Drink("Soda", 1.99, "Carbonated soft drink", "Medium", True))

restaurant.add_order(order1.table_number, order1)
restaurant.add_order(order2.table_number, order2)

for table_number, order in restaurant.tables.items():
    items = [item.get_name() for item in order.get_items()]
    total_cost = order.get_total()
    print(f"Table {table_number}: {items} - Total: ${total_cost:.2f}")