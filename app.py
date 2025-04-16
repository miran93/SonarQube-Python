class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current balance for {self.name}: ${self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance=0):
        if name not in self.accounts:
            self.accounts[name] = Account(name, initial_balance)
            print("Account created successfully.")
        else:
            print("Account already exists.")

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            self.accounts[name].withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, name):
        if name in self.accounts:
            self.accounts[name].check_balance()
        else:
            print("Account not found.")

    def transfer(self, sender_name, receiver_name, amount):
        if sender_name in self.accounts and receiver_name in self.accounts:
            if self.accounts[sender_name].balance >= amount:
                self.accounts[sender_name].withdraw(amount)
                self.accounts[receiver_name].deposit(amount)
                print(f"Transferred ${amount} from {sender_name} to {receiver_name}.")
            else:
                print("Insufficient funds.")
        else:
            print("Sender or receiver account not found.")


def main():
    bank = Bank()

    while True:
        print("\n===== Banking System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)

        elif choice == '2':
            name = input("Enter account holder's name: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(name, amount)

        elif choice == '3':
            name = input("Enter account holder's name: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(name, amount)

        elif choice == '4':
            name = input("Enter account holder's name: ")
            bank.check_balance(name)

        elif choice == '5':
            sender_name = input("Enter sender's name: ")
            receiver_name = input("Enter receiver's name: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer(sender_name, receiver_name, amount)

        elif choice == '6':
            print("Exiting....")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
