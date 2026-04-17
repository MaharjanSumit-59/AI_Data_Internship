"""
Write a Python program that takes a student's marks as input and prints the grade based on the following criteria:
90 and above → A
80 to 89 → B
70 to 79 → C
60 to 69 → D
Below 60 → Fail
"""
try:
    marks = float(input("Enter the student's marks: "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: Fail")
except ValueError:
    print("Invalid input. Please enter a valid number.")