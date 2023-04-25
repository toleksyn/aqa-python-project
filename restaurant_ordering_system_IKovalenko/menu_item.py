
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
