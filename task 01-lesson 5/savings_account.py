from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder_name, balance, interest_rate, minimum_balance):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Cannot withdraw beyond the minimum balance")
        else:
            super().withdraw(amount)
