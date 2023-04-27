# Create a class hierarchy for a restaurant ordering system
# Create an instance of the Restaurant class and add a few orders with multiple items each.
from Omelchenko_Homework6.Restaurant.appetizer import Appetizer
from Omelchenko_Homework6.Restaurant.entree import Entree
from Omelchenko_Homework6.Restaurant.drink import Drink
from Omelchenko_Homework6.Restaurant.order import Order
from Omelchenko_Homework6.Restaurant.restaurant import Restaurant

first_order = Order(1)
first_order.add_item(Appetizer("Canape", 2, "small sandwich with oil and vegetables", False, True))
first_order.add_item(Entree("Soup", 5, "Chicken soup with macaronis", False, True))
first_order.add_item(Drink("Coca-Cola", 1, "Bottle of CocaCola", 0.5, True))
second_order = Order(2)
second_order.add_item(Appetizer("Capreze", 5, "Salad with tomatoes and cheese", False, True))
second_order.add_item(Entree("Steak", 30, "Medium-rare beef steak with cherry sauce", False, False))
second_order.add_item(Drink("Coffee", 2, "A cup of an espresso", 0.1, True))
print(str(first_order))
print(str(second_order))
grill_bar = Restaurant("GrillBar")
grill_bar.add_order(1, first_order)
grill_bar.add_order(2, second_order)
print(str(grill_bar))
