# 4. Drink: A subclass of MenuItem that represents a drink. It should have the following attributes and methods:
#     * size (string)
#     * is_refillable (boolean)
#     * get_size(self): Returns the size of the drink.
#     * is_refillable(self): Returns whether the drink is refillable or not.
#     * str(self): Returns a string representation of the drink object in the format
from Omelchenko_Homework6.Restaurant.menu_item import MenuItem


class Drink(MenuItem):

    def __init__(self, name, price, description, size, is_refillable):
        super().__init__(name, price, description, False)
        self.size = size
        self.is_refillable = is_refillable

    def get_size(self):
        return self.size

    def is_refillable(self):
        return self.is_refillable

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description} ({self.size}l, Refillable: {self.is_refillable})"
