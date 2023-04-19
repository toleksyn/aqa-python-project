from account import Account


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, interest_rate, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            print("Error: Withdraw amount too high.")
        else:
            super().withdraw(amount)

    def calculate_interest(self):
        return self.balance * self.interest_rate
