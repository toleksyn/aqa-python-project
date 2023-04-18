from Bank.bank import Bank
from Zoo.bird import Bird
from Bank.checking_account import CheckingAccount
from Zoo.mammal import Mammal
from Zoo.reptile import Reptile
from Zoo.zookeeper import Zookeeper

# Task 1: Create classes to model various accounts and a bank:
print("Task 1")
privat_bank = Bank("PrivatBank")
privat_bank.list_of_accounts.append(CheckingAccount(1, "John", 1000, 10, 500))
privat_bank.list_of_accounts.append(CheckingAccount(2, "James", 1000, 10, 500))
privat_bank.list_of_accounts.append(CheckingAccount(3, "Johny", 1000, 10, 500))
privat_bank.all_bank_accounts(privat_bank.list_of_accounts)
privat_bank.remove_account(privat_bank.list_of_accounts[2])
privat_bank.all_bank_accounts(privat_bank.list_of_accounts)
print(privat_bank.find_account(2))
print(privat_bank.find_account(3))
print(privat_bank.find_account(4))
privat_bank.total_interests_earned()
# Task 2: Create classes for a zoo that has the following classes:
print("Task 2")
john = Zookeeper("John", 32)
john.list_of_animals.append(Mammal("Dog", "Charlie", 2, "Male", 4))
john.list_of_animals.append(Bird("Parrot", "Rickie", 2, "Female", 1))
john.list_of_animals.append(Reptile("Gecko", "Spicy", 5, "Male", "red"))
print("What is your name and How many animals do you have?")
john.animals_responsibility(john.list_of_animals)
print("What are you doing", john.name + "?")
john.feed_animals(john.list_of_animals[1])
john.clean_habitats(john.list_of_animals[0])

