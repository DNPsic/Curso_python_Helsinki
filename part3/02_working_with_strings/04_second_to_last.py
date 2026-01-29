"""
Please write a program which asks the user for a string. The program then
prints out a message based on whether the second character and the second
to last character are the same or not. See the examples below.
"""

# My solution:

string = input("Please type in a string: ")
second = string[1]
second_last = string[-2]

if second == second_last:
    print("The second and the second to last characters are", second)
else:
    print("The second and the second to last characters are different")

# Model's solution:
# word = input("Please type in a string: ")
#
# # Check also that the word is at least two characters long,
# # so that the second and second to last characters exist
# if len(word) > 1 and word[1] == word[-2]:
#     print("The second and the second to last characters are " + word[1])
# else:
#     print("The second and the second to last characters are different")
