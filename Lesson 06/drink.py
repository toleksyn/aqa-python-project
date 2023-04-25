from menu_item import MenuItem


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
        return f"{self.name} - ${self.price}: {self.description} ({self.size}, Refillable: {self.is_refillable})"
