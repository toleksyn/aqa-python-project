from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, interest_rate, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Cannot withdraw beyond the overdraft limit")
        else:
            self.balance -= amount

    def calculate_interest(self):
        return self.balance * self.interest_rate

