"""
Write a program that asks the user to enter a number and prints its multiplication table from 1 to 10 using a for loop.
"""

try:
    num = int(input("Enter the number for it's multiplication table: "))
    print(f"Multiplication Table of {num}")
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")