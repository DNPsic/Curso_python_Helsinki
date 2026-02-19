"""
Please write a program which asks the user to type in a sentence.
The program then prints out the first letter of each word in the
sentence, each letter on a separate line.
"""

sentence: str = input("Please type in a sentence: ")
word: str = ""
print(sentence[0])
while sentence.find(" ") != -1:
    sentence = sentence[sentence.find(" ") + 1 :]
    print(sentence[0])

# Model's solution
# sentence = input("Please type in a sentence: ")
#
# # Add a space at the start, to make handling sentence easier
# sentence = " " + sentence
#
# # Searching for indexes which are preceded by spaces
# index = 1
# while index < len(sentence):
#     if sentence[index-1] == " " and sentence[index] != " ":
#         print(sentence[index])
#     index += 1
