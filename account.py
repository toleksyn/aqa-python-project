
class Account:
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account {self.account_number}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount} from account {self.account_number}. New balance is {self.balance}.")
        else:
            print(f"Insufficient funds in account {self.account_number} to withdraw {amount}.")
        