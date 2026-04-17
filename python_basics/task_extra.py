# Write a Python program that takes a number as input and checks whether it is even or odd.
"""
def check_even_odd():
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
"""        
        
# Write a program to check if a year entered by the user is a leap year or not.
"""
def check_leap_year():
    try:
        year = int(input("Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")
"""

# Ask the user for a number and print the sum of all numbers from 1 to that number.
"""
def sum_of_numbers():
    try:
        number = int(input("Enter a number: "))
        total_sum = 0
        for i in range(1, number + 1):
            total_sum += i
        print(f"The sum of all numbers from 1 to {number} is: {total_sum}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
"""

# Write a program to print the factorial of a number using a loop.
"""
def factorial():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        elif number == 0 or number == 1:
            print(f"The factorial of {number} is 1.")
        else:
            result = 1
            for i in range(2, number + 1):
                result *= i
            print(f"The factorial of {number} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
"""
 
if __name__ == "__main__":    

    # check_even_odd()
    # check_leap_year()
    # sum_of_numbers()
    # factorial()