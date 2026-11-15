from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully!")

    def check_balance(self):
        print("Current Balance:", self.__balance)

    def display_details(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type())
        print("Balance:", self.__balance)


class SavingsAccount(BankAccount):

    def account_type(self):
        return "Savings Account"

class CurrentAccount(BankAccount):

    def account_type(self):
        return "Current Account"

class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self):

        name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")

        if account_number in self.accounts:
            print("Account number already exists!")
            return

        print("1. Savings Account")
        print("2. Current Account")

        choice = input("Choose account type: ")

        if choice == '1':
            account = SavingsAccount(name, account_number)

        elif choice == '2':
            account = CurrentAccount(name, account_number)

        else:
            print("Invalid account type!")
            return

        self.accounts[account_number] = account

        print("Account created successfully!")

    def get_account(self):

        account_number = input("Enter account number: ")

        if account_number not in self.accounts:
            print("Account not found!")
            return None

        return self.accounts[account_number]

    def deposit_money(self):

        account = self.get_account()

        if account:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

    def withdraw_money(self):

        account = self.get_account()

        if account:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

    def check_balance(self):

        account = self.get_account()

        if account:
            account.check_balance()

    def display_account(self):

        account = self.get_account()

        if account:
            account.display_details()

    def menu(self):

        while True:

            print("\n===== BANK MANAGEMENT SYSTEM =====")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Display Account Details")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()

            elif choice == '2':
                self.deposit_money()

            elif choice == '3':
                self.withdraw_money()

            elif choice == '4':
                self.check_balance()

            elif choice == '5':
                self.display_account()

            elif choice == '6':
                print("Thank you for using our bank!")
                break

            else:
                print("Invalid choice! Try again.")


bank = Bank()
bank.menu()