
from menu_item import MenuItem

class Entree(MenuItem):
    def __init__(self, name, price, description, is_vegetarian, is_gluten_free):
        super().__init__(name, price, description, is_vegetarian)
        self.is_gluten_free = is_gluten_free

    def get_gluten_free(self):
        return self.is_gluten_free

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description} (Vegetarian: {self.is_vegetarian}, Gluten-free: {self.is_gluten_free})"
