"""Please write a program which asks the user for words.
If the user types in a word for the second time, the
program should print out the number of different words
typed in, and exit."""

word_list: list = []
word_count: int = 0

while True:
    word: str = input("Word: ")
    if word in word_list:
        break
    word_list.append(word)
    word_count += 1

print(f"You typed in {word_count} different words")

# Model's slution:
#
# words = []
# while True:
#     word = input("Word: ")
#     if word in words:
#         break
#     words.append(word)
# print("You typed in", len(words), "different words")
