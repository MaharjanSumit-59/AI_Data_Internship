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
class BankAccount:
    def __init__(self):
        self.accounts = {} # To store account details
    def create_account(self):
        name = input("Enter account holder's name: ")
        account_number = input("Enter account number: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        self.accounts[account_number] = {
            "name": name,
            "balance": initial_deposit
        }
        print(f"Account for {name} created successfully with balance ${initial_deposit}.")

            
class User(BankAccount):
    def __init__(self):
        super().__init__()
        self.logged_in_account = None
    def login(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            self.logged_in_account = account_number
            print(f"Welcome {self.accounts[account_number]['name']}!")
        else:
            print("Account number not found.")
    def deposit(self):
        if self.logged_in_account:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.accounts[self.logged_in_account]['balance'] += amount
                print(f"Deposited ${amount}. New balance: ${self.accounts[self.logged_in_account]['balance']}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Please log in to perform this action.")
    def withdraw(self):
        if self.logged_in_account:
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                if amount <= self.accounts[self.logged_in_account]['balance']:
                    self.accounts[self.logged_in_account]['balance'] -= amount
                    print(f"Withdrew ${amount}. New balance: ${self.accounts[self.logged_in_account]['balance']}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        else:
            print("Please log in to perform this action.")
    def check_balance(self):
        if self.logged_in_account:
            print(f"Current balance: ${self.accounts[self.logged_in_account]['balance']}")
        else:
            print("Please log in to perform this action.")
    def logout(self):
        if self.logged_in_account:
            print(f"Goodbye {self.accounts[self.logged_in_account]['name']}!")
            self.logged_in_account = None
        else:
            print("No account is currently logged in.")
            
    def send_money(self):
        if self.logged_in_account:
            recipient_account = input("Enter recipient account number: ")
            if recipient_account in self.accounts:
                amount = float(input("Enter amount to send: "))
                if amount > 0:
                    if amount <= self.accounts[self.logged_in_account]['balance']:
                        self.accounts[self.logged_in_account]['balance'] -= amount
                        self.accounts[recipient_account]['balance'] += amount
                        print(f"Sent ${amount} to {self.accounts[recipient_account]['name']}. New balance: ${self.accounts[self.logged_in_account]['balance']}")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Amount must be positive.")
            else:
                print("Recipient account number not found.")
        else:
            print("Please log in to perform this action.")
            
# Example usage:
bank = User()

while True:
    print("\nBanking System")

    if bank.logged_in_account is None:
        # Menu before login
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

    else:
        # Menu after login
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Send Money")
        print("4. Check Balance")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.deposit()
        elif choice == "2":
            bank.withdraw()
        elif choice == "3":
            bank.send_money()
        elif choice == "4":
            bank.check_balance()
        elif choice == "5":
            bank.logout()
        else:
            print("Invalid choice. Please try again.")
"""