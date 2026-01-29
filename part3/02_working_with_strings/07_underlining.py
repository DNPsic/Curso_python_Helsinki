"""Please write a program which asks the user for strings using a loop.
The program prints out each string underlined as shown in the examples below.
The execution ends when the user inputs an empty string - that is, just
presses Enter at the prompt.
"""

# My solution:

while True:
    in_string = input("Please type in a string: ")
    if in_string == "":
        break
    print(in_string)
    print("-" * len(in_string))
