
from savings_account import SavingsAccount
from checking_account import CheckingAccount

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Added account {account.account_number} to {self.bank_name}.")

    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Removed account {account_number} from {self.bank_name}.")
                return
            print(f"Account {account_number} not found in {self.bank_name}.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"Found account {account_number}.")
                return account
        print(f"Account {account_number} not found in {self.bank_name}.")
        return None

    def calculate_interest_earned(self):
        total_interest_earned = 0
        for account in self.accounts:
            interest_earned = account.balance * (account.interest_rate / 100)
            total_interest_earned += interest_earned
        print(f"Total interest earned by the bank is {total_interest_earned}.")