# 2. Appetizer: A subclass of MenuItem that represents an appetizer. It should have the
# following attributes and methods:
#     * is_spicy (boolean)
#     * get_spiciness(self): Returns whether the appetizer is spicy or not.
#     * str(self): Returns a string representation of the appetizer object in the format
from Omelchenko_Homework6.Restaurant.menu_item import MenuItem


class Appetizer(MenuItem):

    def __init__(self, name, price, description, is_vegetarian, is_spicy):
        super().__init__(name, price, description, is_vegetarian)
        self.is_spicy = is_spicy

    def get_spiciness(self):
        return self.is_spicy

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description} (Vegetarian: {self.is_vegetarian}" \
               f", Spicy: {self.is_spicy})"
