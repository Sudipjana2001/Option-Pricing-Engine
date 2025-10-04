class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        self.accounts[account_number] = Account(account_number, initial_balance)

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            return f"Deposited {amount} into account {account_number}"
        return "Account not found"

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].balance >= amount:
                self.accounts[account_number].balance -= amount
                return f"Withdrew {amount} from account {account_number}"
            return "Insufficient funds"
        return "Account not found"

bank = Bank()
bank.create_account("12345", 1000)

while True:
    print("1. Deposit")
    print("2. Withdraw")
    choice = input("Choose an option: ")
    if choice == "1":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        print(bank.deposit(account_number, amount))
    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        print(bank.withdraw(account_number, amount))
