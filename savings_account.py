
from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, interest_rate, minimum_balance):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print(f"Cannot withdraw {amount} from account {self.account_number} because it would bring the balance below the minimum balance of {self.minimum_balance}.")
        else:
            super().withdraw(amount)

    def calculate_interest(self):
        interest_earned = self.balance * (self.interest_rate / 100)
        print(f"Account {self.account_number} earned {interest_earned} interest.")
