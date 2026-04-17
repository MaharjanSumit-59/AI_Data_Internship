"""
Write a Python program that reads a text file and counts the total number of words in it.Handle the case where the file does not exist using exception handling.
"""

try:
    file_name = input("Enter the name of the text file (with extension): ")
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        print(f"The total number of words in the file is: {word_count}")
except FileNotFoundError:
    print("The file does not exist. Please check the file name and try again.")