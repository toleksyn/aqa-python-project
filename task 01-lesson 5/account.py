class Account:
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
