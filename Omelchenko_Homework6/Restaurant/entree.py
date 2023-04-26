# 3. Entree: A subclass of MenuItem that represents an entree. It should have the following attributes and methods:
#     * is_gluten_free (boolean)
#     * get_gluten_free(self): Returns whether the entree is gluten-free or not.
#     * str(self): Returns a string representation of the entree object in the format
#     ""[name] - $[price]: [description] (Vegetarian: [True/False], Gluten-free: [True/False])"".
from Omelchenko_Homework6.Restaurant.menu_item import MenuItem


class Entree(MenuItem):

    def __init__(self, name, price, description, is_vegetarian, is_gluten_free):
        super().__init__(name, price, description, is_vegetarian)
        self.is_gluten_free = is_gluten_free

    def get_gluten_free(self):
        return self.is_gluten_free

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description} (Vegetarian: {self.is_vegetarian}" \
               f", Gluten-free: {self.is_gluten_free})"
