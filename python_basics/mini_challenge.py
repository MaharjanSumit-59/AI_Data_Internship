# Design a class ATM with login, deposit, withdraw, and balance check features.
"""
class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.logged_in = False # To track login status
    def login(self):
        input_pin = input("Enter your PIN: ")
        if input_pin == self.pin:
            self.logged_in = True
            print("Login successful.")
        else:
            print("Invalid PIN. Please try again.")
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if self.logged_in:
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance: ${self.balance}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Please log in to perform this action.")
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.logged_in:
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Withdrew ${amount}. New balance: ${self.balance}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        else:
            print("Please log in to perform this action.")
    def check_balance(self):
        if self.logged_in:
            print(f"Current balance: ${self.balance}")
        else:
            print("Please log in to perform this action.")

# Example usage:
user1 = ATM(pin="1234", balance=1000)
user2 = ATM(pin="5678", balance=500)

user1.login()
user1.deposit()
user1.check_balance()
user1.withdraw()
user1.check_balance()

"""

