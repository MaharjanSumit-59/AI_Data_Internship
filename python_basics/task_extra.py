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

# Create a function that checks whether a number is prime or not.
"""
def check_prime():
    try:
        number = int(input("Enter a number: "))
        if number <= 1:
            print(f"{number} is not a prime number.")
        else:
            is_prime = True
            for i in range(2, int(number**0.5) + 1): 
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
"""

# Write a function that accepts a list and returns the sum of all elements.
"""
def sum_of_list():
    numbers = []
    try: 
        n = int(input("Enter the number of elements in the list: "))
        for i in range(n):
            num = float(input(f"Enter element {i + 1}: "))
            numbers.append(num)

        total_sum = sum(numbers)
        print(f"The sum of all elements in the list is: {total_sum}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
"""

# Write a program that takes a list of numbers and prints only the even numbers.
"""
def print_even_numbers():
    number = []
    try:
        n = int(input("Enter the number of elements in the list: "))
        for i in range(n):
            num = int(input(f"Enter element {i + 1}: "))
            number.append(num)
        
        even_numbers = [num for num in number if num % 2 == 0] # num is the variable that represents each element in the list "number". The list comprehension iterates through each element in the list "number" and checks if it is even (num % 2 == 0). If it is even, it is included in the new list "even_numbers".
        print(f"The even numbers in the list are: {even_numbers}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
"""

# Create a function that reverses a list without using built-in reverse methods.
"""
def reverse_list():
    numbers = []
    try:
        n = int(input("Enter the number of elements in the list: "))
        for i in range(n):
            num = input(f"Enter element {i + 1}: ")
            numbers.append(num)

        reversed_list = []
        for i in range(len(numbers) - 1, -1, -1): # This loop starts from the last index of the list (len(numbers) - 1) and goes down to the first index (0) in reverse order. The step -1 indicates that we want to decrement the index by 1 in each iteration, effectively iterating through the list backwards.
            reversed_list.append(numbers[i])

        print(f"The reversed list is: {reversed_list}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
"""

# Write a program to find the second largest number in a list.
"""
def second_largest():
    numbers = []
    try:
        n = int(input("Enter the number of elements in the list: "))
        for i in range(n):
            num = int(input(f"Enter element {i + 1}: "))
            numbers.append(num)
        
        numbers.sort()
        if len(numbers) < 2:
            print("There should be at least two numbers in the list to find the second largest.")
        else:
            second_largest_number = numbers[-2] # The second largest number will be the second last element in the sorted list.
            print(f"The second largest number in the list is: {second_largest_number}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
"""

# Write a program that writes user input to a file and then reads it back.
"""
def write_and_read_file():
    try:
        filename = input("Enter the filename: ")
        content = input("Enter the content to write to the file: ")

        with open(filename, 'w' ) as file: 
            file.write(content)
        print(f"Content written to {filename} successfully.")
        with open(filename, 'r') as file:
            read_content = file.read()
        print(f"Content read from {filename}: {read_content}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
"""
# Create a program that counts the number of lines in a file.
"""
def count_lines_in_file():
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            lines = file.readlines()
        line_count = len(lines)
        print(f"The number of lines in {filename} is: {line_count}")
    except FileNotFoundError:
        print(f"File {filename} not found.")    
"""            
        
# Write a program that copies the contents of one file to another file.
"""
def copy_file():
    try:
        source_filename = input("Enter the source filename: ")
        destination_filename = input("Enter the destination filename: ")
        with open(source_filename, 'r') as source_file:
            content = source_file.read()
        with open(destination_filename, 'w') as destination_file:
            destination_file.write(content)
        print(f"Content copied from {source_filename} to {destination_filename} successfully.")
    except FileNotFoundError:
        print(f"File {source_filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
"""

if __name__ == "__main__":    

    # check_even_odd()
    # check_leap_year()
    # sum_of_numbers()
    # factorial()
    # check_prime()
    # sum_of_list()
    # print_even_numbers()
    # reverse_list()
    # second_largest()
    # write_and_read_file()
    # count_lines_in_file()
    # copy_file()