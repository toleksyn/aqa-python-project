# 2. SavingsAccount: This class should inherit from Account and should have an additional attribute
# called minimum balance. It should override the withdraw method to ensure that
# the balance never goes below the minimum balance.
from Bank.account import Account


class SavingsAccount(Account):

    def __init__(self, account_number, account_holder_name, balance, interest_rate, minimum_balance):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.minimum_balance = minimum_balance

    def withdraw_money(self):
        if self.balance > self.minimum_balance:
            print("You can withdraw $", self.balance)
        else:
            print("Your balance is less than minimum balance")
