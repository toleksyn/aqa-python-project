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
        table_numbers = list(self.tables.keys())
        return f"Restaurant: {self.name}, Tables: {table_numbers}"
