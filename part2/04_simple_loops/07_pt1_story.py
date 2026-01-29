"""
Please write a program which keeps asking the user for words.
If the user types in end, the program should print out the story
the words formed, and finish.
"""

# My solution:
words = ""

while True:
    word = input("Please type in a word: ")
    if word != "end":
        words += word + " "
    else:
        break

print(words)
