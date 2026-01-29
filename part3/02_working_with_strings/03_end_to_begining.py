"""
Please write a program which asks the user for a string.
The program then prints out the input string in reversed order,
from end to beginning. Each character should be on a separate line.
"""

# My solution:

input_string = input("Please type in a string: ")
index = -1

while -len(input_string) < index:
    print(input_string[index])
    index -= 1

# Model's solution:
# input_string = input("Please type in a string: ")
# index = -1
# while index >= -len(input_string):
#     print(input_string[index])
#     index -= 1
