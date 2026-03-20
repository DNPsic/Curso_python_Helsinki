"""Please write three functions: first_word, second_word and last_word.
Each function takes a string argument.
As their names imply, the functions return either the first, the second
or the last word in the sentence they receive as their string argument.
In each case you may assume the argument string contains at least two
separate words, and all words are separated by exactly one space character.
There will be no spaces in the beginning or at the end of the argument strings.
"""


def first_word(sentence: str):
    if sentence.find(" ") == -1:
        return sentence
    first_word = sentence[: sentence.find(" ")]
    return first_word


def second_word(sentence: str):
    second_word = sentence[sentence.find(" ") + 1 :]
    return first_word(second_word)


def last_word(sentence: str):
    while sentence.find(" ") != -1:
        if not sentence.find(" "):
            return sentence
        sentence = sentence[sentence.find(" ") + 1 :]
    return sentence


if __name__ == "__main__":
    sentence = "it was a dark and stormy python"

    print(first_word(sentence=sentence))
    print(second_word(sentence=sentence))
    print(last_word(sentence=sentence))

    sentence = "it was"

    print(second_word(sentence=sentence))
    print(last_word(sentence=sentence))
