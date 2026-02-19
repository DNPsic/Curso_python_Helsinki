"""Please make an extended version of the previous program, which prints out all the substrings
which are at least three characters long, and which begin with the character specified by the user.
You may assume the input string is at least three characters long."""

# word = input("Word: ")
# char = input("character: ")
# index = 0
#
# while True:
#     print(
#         f"Current word: {word} (len: {len(word)}), index of char {char}: {word.find(char)}"
#     )
#     index = word.find(char)
#     if index == -1 or len(word) < index + 3:
#         break
#     print(word[index : index + 3])
#     word = word[index + 1 :]

# Model's solution:
model_word = input("Please type in a word: ")
model_character = input("Please type in a character: ")

model_index = 0

while model_index + 3 <= len(model_word):
    print(f"Index of {model_character}: {model_index}")
    print(f"Len: {len(model_word)}, Index + 3: {model_index + 3}")
    if model_word[model_index] == model_character:
        print(model_word[model_index : model_index + 3])
    model_index += 1
