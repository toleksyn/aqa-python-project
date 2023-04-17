
from savings_account import SavingsAccount
from checking_account import CheckingAccount
from bank import Bank

# create a new bank
my_bank = Bank("My Bank")

# create some accounts
account_one = SavingsAccount("AB12345", "John Doe", 5000, 0.1, 1000)
account_two = CheckingAccount("WS56789", "Rose Robertson", 10000, 0.05, 5000)

# add the accounts to the bank
my_bank.add_account(account_one)
my_bank.add_account(account_two)

# Find an account by account number
account = my_bank.find_account('AB12345')

# make some deposits
account_one.deposit(1000)
account_two.deposit(4000)

# make some withdrawals
account_one.withdraw(2000)
account_two.withdraw(15000)

# calculate interest earned by the account
account_one.calculate_interest()
account_two.calculate_interest()

# calculate interest earned by the bank
my_bank.calculate_interest_earned()

# remove an account from the bank
my_bank.remove_account('AB12345')

# try to find the removed account (should fail)
account = my_bank.find_account('AB12345')