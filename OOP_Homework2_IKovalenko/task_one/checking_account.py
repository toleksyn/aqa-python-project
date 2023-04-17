
from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, interest_rate, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            super().withdraw(amount)
            if self.balance < 0:
                print(f"Account {self.account_number} has overdraft balance of {abs(self.balance)}.")
        else:
            print(
                f"Cannot withdraw {amount} from account {self.account_number} because it exceeds the overdraft limit of {self.overdraft_limit}.")

    def calculate_interest(self):
        interest_earned = self.balance * (self.interest_rate / 100)
        print(f"Account {self.account_number} earned {interest_earned} interest.")