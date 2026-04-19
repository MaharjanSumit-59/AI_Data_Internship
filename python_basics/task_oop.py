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