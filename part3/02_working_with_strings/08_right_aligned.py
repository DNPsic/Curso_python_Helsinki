"""Please write a program which asks the user for a string and then
prints it out so that exactly 20 characters are displayed. If the
input is shorter than 20 characters, the beginning of the line is
filled in with * characters.
"""

# My solution:

in_string = input("Please type in a string: ")
print(f"{'*' * (20 - len(in_string))}{in_string}")

# Model's solution:
# word = input("Please type in a string: ")
#
# aligned = (20 - len(word)) * "*" + word
#
# print(aligned)
