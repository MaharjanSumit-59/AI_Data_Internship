"""
Create a function that accepts a list of numbers and returns the largest number without using Python's built-in max() function.
"""

def max_number():
    try:
        number = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
        if not number:
            print("The list is empty. Please enter at least one number.")
            return None
        max_num = number[0]
        for num in number:
            if num > max_num:
                max_num = num
        return max_num
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None
    
largest_number = max_number()
if largest_number is not None:
    print(f"The largest number in the list is: {largest_number}")