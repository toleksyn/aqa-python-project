# 1. MenuItem: A base class that represents a menu item. It should have the following attributes and methods:
#    * name (string)
#    * price (float)
#    * description (string)
#    * is_vegetarian (boolean)
#     * get_name(self): Returns the name of the menu item.
#     * get_price(self): Returns the price of the menu item.
#     * get_description(self): Returns the description of the menu item.
#     * is_vegetarian(self): Returns whether the menu item is vegetarian.
#     * str(self): Returns a string representation of the menu item object
class MenuItem:

    def __init__(self, name, price, description, is_vegetarian):
        self.name = name
        self.price = price
        self.description = description
        self.is_vegetarian = is_vegetarian

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def is_vegetarian(self):
        return self.is_vegetarian

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description} (Vegetarian: {self.is_vegetarian})"
