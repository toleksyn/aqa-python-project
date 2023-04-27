# 5. Order: A class that represents a customer order. It should have the following attributes and methods:
#     * table_number (integer)
#     * items (list of MenuItem objects)
#     * add_item(self, item): Adds a menu item to the order.
#     * remove_item(self, item): Removes a menu item from the order.
#     * get_items(self): Returns a list of all items in the order.
#     * get_total(self): Returns the total cost of the order.
#     * str(self): Returns a string representation of the order object in the format
class Order:

    def __init__(self, table_number):
        self.items = []
        self.table_number = table_number

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        items = []
        for item in self.items:
            items.append(item.name)
        return items

    def get_total(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return f"Order Total: ${total_price}"

    def __str__(self):
        return f"Table {self.table_number}: {self.get_items()} - {self.get_total()}"
