"""
Change the program so that the loop ends also if the user
types in the same word twice in a row.
"""

words = ""
last_word = ""

while True:
    word = input("Please type in a word: ")
    if word == last_word:
        break
    if word != "end":
        words += word + " "
        last_word = word
    else:
        break

print(words)

# Model's solution:
# story = ""
# previous = ""
# while True:
#     word = input("Please type in a word: ")
#     if word == "end" or word == previous:
#         break
#     story += word + " "
#     previous = word
#
# print(story)
