# 3. CheckingAccount: This class should inherit from Account and should have an additional attribute
# called overdraft limit. It should override the withdraw method to allow the account holder to withdraw
# up to the overdraft limit. It should also have a method to calculate the interest earned on the balance.
from account import Account


class CheckingAccount(Account):

    def __init__(self, account_number, account_holder_name, balance, interest_rate, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance, interest_rate)
        self.overdraft_limit = overdraft_limit

    def withdraw_money(self):
        if amount < self.overdraft_limit:
            self.balance -= amount
            return f'You withdraw {amount}, your current balance is {self.balance}'
        else:
            return f'Withdraw amount {amount} higher than your overdraft limit {self.overdraft_limit}'

    def interest_earned(self):
        print("You've earned", self.interest_rate, "interests")
