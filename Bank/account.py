# 1. Account: This class should represent a bank account and should have the following attributes: account number,
# account holder name, balance, and interest rate. It should also have methods to deposit and withdraw money.
from abc import abstractmethod


class Account:

    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit_money(self, amount):
        self.balance += amount
        return f'You deposit "{amount}". Your current balance is {self.balance}'

    @abstractmethod
    def withdraw_money(self):
        pass
