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

# Write a program where different classes (Bird, Airplane) have the same method fly() but behave differently.
"""
class Bird:
    def fly(self):
        print("The bird is flying with its wings.")
class Airplane:
    def fly(self):
        print("The airplane is flying with its engines.")
class Fish:
    def fly(self):
        print("Fish cannot fly, it swims in water.")
        
bird = Bird()
airplane = Airplane()
fish = Fish()
bird.fly() # Output: The bird is flying with its wings.
airplane.fly() # Output: The airplane is flying with its engines. 
fish.fly() # because of polymorphism, the same method name fly() behaves differently based on the object that calls it.
"""

# Create a function that takes different shapes and calls their area() method (demonstrate polymorphism).
"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    print(f"The area of the shape is: {shape.area()}")

circle = Circle(5)
square = Square(4)
triangle = Triangle(4, 6)
calculate_area(circle) # Output: The area of the shape is: 78.5  
calculate_area(square) # Output: The area of the shape is: 16
calculate_area(triangle) # Output: The area of the shape is: 12.0
"""

# Implement method overloading (simulate it in Python using default arguments).
"""
class Calculator:
    def add(self, a, b, c=0): # c is an optional parameter with a default value of 0.
        return a + b + c
    def multiply(self, *numbers): # using *args to allow for a variable number of arguments for multiplication.
        result = 1
        for num in numbers:
            result *= num
        return result
calc = Calculator() 
print(calc.add(5, 3)) # Output: 8 (using the add method with two parameters)
print(calc.add(5, 3, 2)) # Output: 10 (using the add method with three parameters)

print(calc.multiply(2,3,3,5)) # Output: 90 (using the multiply method with four parameters)
"""

# Create an abstract class Vehicle with an abstract method start(). Implement it in subclasses like Car and Bike.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("The car is starting with a key.")
class Bike(Vehicle):
    def start(self):
        print("The bike is starting with a kick.")
# vve = Vehicle() # This will raise an error because we cannot create an object of an abstract class.
car = Car()
bike = Bike()   
car.start() # Output: The car is starting with a key.
bike.start() # Output: The bike is starting with a kick.
"""

# Write an abstract class Payment with a method pay(). Implement classes like CashPayment and CardPayment.
"""
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} in cash.")
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} with a card.")
        
cashpay = CashPayment()
cardpay = CardPayment()
cashpay.pay(100) # Output: Paying 100 in cash.
cardpay.pay(150) # Output: Paying 150 with a card.
"""

# Write a class Book that initializes title and author using a constructor.
"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
        
book1 = Book("To kill a Mockingbird", "Harper Lee")
book1.display_info()
"""

# Create a class that prints a message when an object is created and another when it is deleted.
"""
class Message:
    def __init__(self, message):
        self.message = message
        print(f"Message created: {self.message}")
    def __del__(self):
        print(f"Message deleted: {self.message}")

msg = Message("Hello, World!")
"""

# Create a class Library that can add books, remove books, and display all books.
"""
class Library:
    def __init__(self):
        self.books = [] # initializing an empty list to store the books in the library.
    def add_book(self, book):
        self.books.append(book) # adding a book to the library by appending it to the books list.
        print(f"Book '{book}' added to the library.")
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book) # removing a book from the library if it exists in the books list.
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")
    def display_books(self):
        if self.books: # checking if there are any books in the library before displaying them.
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")
library = Library()
library.display_books()
library.add_book("Hello, Python!")
library.add_book("Learning OOP")
library.add_book("Python Programming")
library.add_book("Data Structures in Python")
library.display_books()
library.remove_book("Hello, Python!")
library.display_books()
"""

# Build a simple ShoppingCart class that can add items, remove items, and calculate total price.
"""
class ShoppingCart:
    def __init__(self):
        self.items = {} # initializing an empty dictionary to store items and their prices in the shopping cart.
    def add_item(self, item, price):
        self.items[item] = price # adding an item to the shopping cart by setting the item as a key and its price as the value in the items dictionary.
        print(f"Item '{item}' added to the shopping cart with price {price}.")
    def remove_item(self, item):
        if item in self.items:
            del self.items[item] # removing an item from the shopping cart if it exists in the items dictionary.
            print(f"Item '{item}' removed from the shopping cart.")
        else:
            print(f"Item '{item}' not found in the shopping cart.")
    def calculate_total(self):
        total = sum(self.items.values()) # calculating the total price by summing the values (prices) in the items dictionary.
        print(f"Total price of items in the shopping cart: {total}")

cart = ShoppingCart()
cart.add_item("Laptop", 1000)
cart.add_item("Headphones", 200)
cart.add_item("Mouse", 50)
cart.calculate_total()
cart.remove_item("Headphones")
cart.calculate_total()
"""

# Write a class Timer that starts, stops, and shows elapsed time.
"""
class Timer:
    import time
    def __init__(self):
        self.start_time = None
        self.end_time = None
    def start(self):
        self.start_time = self.time.time() # recording the start time using the time module.
        print("Timer started.")
    def stop(self):
        if self.start_time is not None:
            self.end_time = self.time.time() # recording the end time using the time module.
            print("Timer stopped.")
        else:
            print("Timer has not been started yet.")
    def elapsed_time(self):
        if self.start_time is not None and self.end_time is not None:
            elapsed = self.end_time - self.start_time # calculating the elapsed time by subtracting the start time from the end time.
            print(f"Elapsed time: {elapsed:.2f} seconds.")
        else:
            print("Timer has not been started and stopped properly.")
            
timer = Timer()
timer.start()
timer.time.sleep(2) # simulating a delay of 2 seconds to demonstrate the timer functionality.       
timer.stop()
timer.elapsed_time()
"""