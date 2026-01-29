"""Please write a program which asks the user to type in a string.
The program then prints out all the substrings which begin with the
first character, from the shortest to the longest."""

# My solution:
word = input("Please type in a string: ")
length = 0
while len(word) >= length:
    print(word[0:length])
    length += 1
