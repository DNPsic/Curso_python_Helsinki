"""Please write a program which asks the user to type in a string.
The program then prints out all the substrings which begin with the
first character, from the shortest to the longest."""

# My solution:
word = input("Please type in a string: ")
length = -1
while -len(word) <= length:
    print(word[length:])
    length -= 1

# Model's solution:
# string = input("Please type in a string: ")
#
# start = len(string) - 1
# while start >= 0:
#     print(string[start:])
#     start -= 1
