# 2. SavingsAccount: This class should inherit from Account and should have an additional attribute
# called minimum balance. It should override the withdraw method to ensure that
# the balance never goes below the minimum balance.
from account import Account


class SavingsAccount(Account):

    def __init__(self, account_number, account_holder_name, balance, interest_rate, minimum_balance):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.minimum_balance = minimum_balance

    def withdraw_money(self, amount):
        if self.balance > self.minimum_balance and (self.balance-amount) > self.minimum_balance:
            self.balance -= amount
            return f'You withdraw {amount}, your current balance is {self.balance}'
        else:
            return f'You can not withdraw "{amount}" since balance after withdrawing "{self.balance-amount}"' \
                   f' will be less than minimum "{self.minimum_balance}"'
