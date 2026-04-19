# Write a class Student with attributes name and marks. Create objects and display their details.
"""
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Student's name is {self.name} and marks are {self.marks}.")
        
        
sumit = student("Sumit", 85)
ram = student("Ram", 90)
sumit.display()
ram.display()
"""

# Create a class Car with attributes like brand and speed. Add a method to display car info.
"""
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def display_info(self):
        print(f"The car brand is {self.brand} and its speed is {self.speed} km/h.")
        
car1 = Car("Bugatti", 420)
car1.display_info()

car2 = Car("Ferrari", 350)
car2.display_info()
"""

# Write a class Rectangle with methods to calculate area and perimeter.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is {area}.")
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"The perimeter of the rectangle is {perimeter}.")
        
rec1 = Rectangle(5, 3)
rec1.area()
rec1.perimeter()
"""

# Create a class BankAccount with a private balance. Add methods to deposit and withdraw money safely.
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # balance is private because of double underscore
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance is {self.__balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
            
account = BankAccount(0)
account.withdraw(50)
account.deposit(100)
account.withdraw(30)
"""

# Write a class Person where age cannot be set to a negative value (use setter methods).
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age if age >= 0 else 0 # age is private and cannot be negative
    def set_age(self, age):
        if age >= 0:
            self.__age = age
            print(f"Age set to {self.__age}.")
        else:
            print("Age cannot be negative.")
person1 = Person("Alice", 25)
person1.set_age(30) # Valid age
person1.set_age(-5) # Invalid age       
"""

# Create a class PasswordManager that hides the password and allows only validation, not direct access.
"""
class PasswordManager:
    def __init__(self, password):
        self.__password = password # password is made private for security reasons and cannot be accessed directly when creating an object of the class.
    def validate_password(self, input_password):
        if input_password == self.__password:
            print("Password is valid.")
        else:
            print("Invalid password.")
            
manager = PasswordManager("my_secure_password")
manager.validate_password("my_secure_password") # Valid password
manager.validate_password("wrong_password") # Invalid password
print(manager.__password) # This will raise an AttributeError because __password is private and cannot be accessed directly.
"""