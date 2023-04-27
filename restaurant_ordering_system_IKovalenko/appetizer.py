from menu_item import MenuItem

class Appetizer(MenuItem):
    def __init__(self, name, price, description, is_vegetarian, is_spicy):
        super().__init__(name, price, description, is_vegetarian)
        self.is_spicy = is_spicy

    def get_spiciness(self):
        return self.is_spicy

    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description} (Vegetarian: {self.is_vegetarian}, Spicy: {self.is_spicy})"
