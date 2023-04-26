# 6. Restaurant: A class that represents a restaurant. It should have the following attributes and methods:
#     * name (string)
#     * tables (dictionary where key is table number and value is Order object)
#     * add_order(self, table_number, order): Adds an order to a table.
#     * remove_order(self, table_number): Removes the order from a table.
#     * get_orders(self): Returns a dictionary of all orders in the restaurant.
#     * str(self): Returns a string representation of the restaurant object in the format
#     "Restaurant: [name], Tables: [list of table numbers]".
class Restaurant:

    def __init__(self, name):
        self.name = name
        self.tables = {}

    def add_order(self, table_number, order):
        self.tables[table_number] = order

    def remove_order(self, table_number):
        del self.tables[table_number]

    def get_orders(self):
        return self.tables

    def __str__(self):
        table_numbers = 0
        for table_number, order in self.tables.items():
            table_numbers = table_number
        return f"Restaurant: {self.name}, Tables: {table_numbers}"
