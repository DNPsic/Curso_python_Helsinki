"""Please write a function named same_chars, which takes
one string and two integers as arguments. The integers refer
to indexes within the string. The function should return True
if the two characters at the indexes specified are the same.
Otherwise, and especially if either of the indexes falls outside
the scope of the string, the function returns False."""


def same_chars(word: str, index1, index2):
    if len(word) - 1 < index1:
        # print(f"Index {index1} out of '{word}' string.")
        # print(f"The word '{word}' has only {len(word) - 1} indexes!")
        return False

    if len(word) - 1 < index2:
        # print(f"Index {index2} out of '{word}' string.")
        # print(f"The word '{word}' has only {len(word) - 1} indexes!")
        return False

    char1 = word[index1]
    char2 = word[index2]

    if word.find(char1) == word.find(char2):
        # print(f"The characters '{char1}' and '{char2}' are the same!")
        return True

    if word.find(char1) != word.find(char2):
        # print(f"The characters '{char1}' and '{char2}' are the different!")
        return False


# def same_chars(str, a, b):
#     if a >= len(str) or b >= len(str):
#         return False
#     return str[a] == str[b]

if __name__ == "__main__":
    same_chars("hola", 4, 1)
    same_chars("hola", 0, 4)
    same_chars("cerebros", 1, 3)
    same_chars("cerebros", 0, 3)
