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
    
    def print_orders(self, table_number):
        if table_number in self.tables:
            orders = self.tables[table_number]
            print(f"Orders for table {table_number}: {orders}")
        else:
            print(f"No orders found for table {table_number}")

    def __str__(self):
        table_numbers = list(self.tables.keys())
        return f"Restaurant: {self.name}, Tables: {table_numbers}"
