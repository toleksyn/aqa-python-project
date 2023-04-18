# 4. Bank: This class should represent a bank and should have a list of accounts.
# It should have methods to add and remove accounts, as well as to find accounts by account number.
# It should also have a method to calculate the total interest earned on all accounts.
class Bank:

    def __init__(self, name):
        self.name = name
        self.list_of_accounts = []

    def add_account(self, account):
        self.list_of_accounts.append(account)

    def remove_account(self, account):
        self.list_of_accounts.remove(account)

    def all_bank_accounts(self, account):
        print(self.name, "has such account holders")
        for account in self.list_of_accounts:
            print(account.account_holder_name, "with", account.balance, "balance")

    def find_account(self, account_number):
        for account in self.list_of_accounts:
            if account.account_number == account_number:
                return "Account holder: " + account.account_holder_name
        return "Account with " + "'" + str(account.account_number) + "'" + " account number doesn't exist"

    def total_interests_earned(self):
        total_interests = 0
        for account in self.list_of_accounts:
            total_interests += account.interest_rate
        print("Total interest earned from all accounts", total_interests)

