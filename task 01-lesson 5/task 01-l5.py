from account import Account
from savings_account import SavingsAccount
from checkinga_ccount import CheckingAccount
from bank import Bank

account_main = Account(1, "Viktor Nesterenko", 1000, 0.02)
account_sav = SavingsAccount(2, "Robin Hood", 500, 0.01, 100)
account_check = CheckingAccount(3, "Bart Simpson", 2000, 0.03, 500)

bank = Bank()
bank.add_account(account1)
bank.add_account(account2)
bank.add_account(account3)

print(bank.total_interest_earned())

account = bank.find_account(1)
account.withdraw(250)
print(account.balance)

account = bank.find_account(2)
account.withdraw(666)

account = bank.find_account(3)
print(account.calculate_interest())
