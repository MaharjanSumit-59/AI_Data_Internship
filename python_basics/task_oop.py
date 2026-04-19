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

# Create a base class Animal with a method sound(). Derive classes like Dog and Cat that override it.
"""
class Animal:
    # there is no need to create an init method in the base class because we are not initializing any attributes in the base class.
    def sound(self):
        print("Animal makes a sound.")
    
class Dog(Animal):
    def sound(self):
        print("Dog barks.")
class Cat(Animal):
    def sound(self):
        print("Cat meows.")
        
dog = Dog()
cat = Cat()
animal = Animal()
animal.sound() # Output: Animal makes a sound.
dog.sound() # Output: Dog barks.
cat.sound() # Output: Cat meows.    
"""

# Write a class Employee and a subclass Manager that adds extra attributes like bonus.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary) # calling the init method of the base class to initialize name and salary attributes.
        self.bonus = bonus
        
manager = Manager("John", 50000, 10000)
print(f"Manager's name: {manager.name}")    
print(f"Manager's salary: {manager.salary}")
print(f"Manager's bonus: {manager.bonus}")      
"""

# Create a class Shape and derive Circle and Square with their own area methods.
"""
class shape:
    def area(self):
        if type(self) == Circle: # checking the type of the object to determine which area method to call.
            return 3.14 * self.radius ** 2
        else:
            return self.side ** 2
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return super().area()
class Square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return super().area()
    
circle = Circle(5)
square = Square(4)
print(f"Area of the circle: {circle.area()}") # Output: Area of the circle: 78.5
print(f"Area of the square: {square.area()}") # Output: Area of the square: 16
"""