
from appetizer import Appetizer
from entree import Entree
from drink import Drink

class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def get_total(self):
        return sum(item.get_price() for item in self.items)

    def __str__(self):
        item_names = [item.get_name() for item in self.items]
        return f"Table {self.table_number}: {item_names} - Total: ${self.get_total()}"