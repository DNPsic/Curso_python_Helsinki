"""
Please write a program which asks the user for two strings and then
prints out whichever is the longer of the two - that is, whichever has
the more characters. If the strings are of equal length, the program
should print out "The strings are equally long".
"""

# My solution:

first_string = input("Please type in string 1: ")
second_string = input("Please type in string 2: ")

if len(first_string) > len(second_string):
    print(f"{first_string} is longer")
elif len(first_string) < len(second_string):
    print(f"{second_string} is longer")
else:
    print("The strings are equally long")

# Model's solution:
# input_string1 = input("Please type in string 1: ")
# input_string2 = input("Please type in string 2: ")
#
# if len(input_string1) > len(input_string2):
#     print(input_string1, "is longer")
# elif len(input_string2) > len(input_string1):
#     print(input_string2, "is longer")
# else:
#     print("The strings are equally long")
