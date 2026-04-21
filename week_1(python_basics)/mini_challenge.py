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

# Create a mini student management system using classes (add, remove, search students).
"""
class Student:
    def __init__(self):
        self.students = {} # To store student records
    def add_student(self):
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        student_id = input("Enter student ID: ")
        department = input("Enter student department: ")
        self.students[student_id] = {
            "name": name,
            "age": age,
            "department": department
        }
        print(f"Student {name} added successfully.")
    def remove_student(self):
        student_id = input("Enter student ID to remove: ")
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Student {removed_student} removed successfully.")
        else:
            print("Student ID not found.")
    def search_student(self):
        student_id = input("Enter student ID to search: ")
        if student_id in self.students:
            student_info = self.students[student_id]
            print(f"Student found: {student_info}")
        else:
            print("Student ID not found.")
    def display_students(self):
        if self.students:
            print("Student List:")
            for student_id, info in self.students.items():
                print(f"ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Department: {info['department']}")

            
        
# Example usage:
std1 = Student()
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        std1.add_student()
    elif choice == "2":
        std1.remove_student()
    elif choice == "3":
        std1.search_student()
    elif choice == "4":
        std1.display_students()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
"""

# Build a simple banking system with multiple accounts and transactions.
"""

class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number, initial_deposit):
        if account_number in self.accounts:
            print("Account number already exists.")
            return

        self.accounts[account_number] = Account(name, account_number, initial_deposit)
        print(f"Account created for {name} with balance ${initial_deposit}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)


class Session:
    def __init__(self, bank):
        self.bank = bank
        self.current_account = None

    def login(self):
        acc_no = input("Enter account number: ")
        account = self.bank.get_account(acc_no)

        if account:
            self.current_account = account
            print(f"Welcome {account.name}!")
        else:
            print("Account not found.")

    def logout(self):
        if self.current_account:
            print(f"Goodbye {self.current_account.name}")
            self.current_account = None

    def deposit(self):
        amount = float(input("Enter amount: "))
        if amount > 0:
            self.current_account.balance += amount
            print(f"New balance: ${self.current_account.balance}")
        else:
            print("Invalid amount")

    def withdraw(self):
        amount = float(input("Enter amount: "))
        if 0 < amount <= self.current_account.balance:
            self.current_account.balance -= amount
            print(f"New balance: ${self.current_account.balance}")
        else:
            print("Invalid or insufficient funds")

    def send_money(self):
        target_no = input("Enter recipient account number: ")
        target = self.bank.get_account(target_no)

        if not target:
            print("Recipient not found")
            return

        amount = float(input("Enter amount: "))

        if 0 < amount <= self.current_account.balance:
            self.current_account.balance -= amount
            target.balance += amount
            print(f"Sent ${amount} to {target.name}")
        else:
            print("Invalid or insufficient funds")

    def check_balance(self):
        print(f"Balance: ${self.current_account.balance}")


# ---- MAIN PROGRAM ----
bank = Bank()
session = Session(bank)

while True:
    print("\n=== Banking System ===")

    if session.current_account is None:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            acc_no = input("Account Number: ")
            deposit = float(input("Initial Deposit: "))
            bank.create_account(name, acc_no, deposit)

        elif choice == "2":
            session.login()

        elif choice == "3":
            break

        else:
            print("Invalid choice")

    else:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Send Money")
        print("4. Check Balance")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            session.deposit()
        elif choice == "2":
            session.withdraw()
        elif choice == "3":
            session.send_money()
        elif choice == "4":
            session.check_balance()
        elif choice == "5":
            session.logout()
        else:
            print("Invalid choice")
""" 