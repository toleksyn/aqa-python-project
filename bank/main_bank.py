from savings_account import SavingsAccount
savings_account = SavingsAccount("001", "Jack Smith", 3000, 0.1, 500)
savings_account.withdraw(3000)
print(savings_account.balance)

from checking_account import CheckingAccount
checking_account = CheckingAccount("002", "Lia Wu", 5000, 0.07, 1000)
checking_account.withdraw(500)
print(checking_account.calculate_interest())

from bank import Bank
bank = Bank()
bank.add_account(savings_account)
bank.add_account(checking_account)
print(bank.total_interest_earned())

# Find account by account number
account = bank.find_account("001")
print(account.account_holder_name)

bank.remove_account(savings_account)
