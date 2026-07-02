"""Please write a function named histogram, which takes a string as
its argument. The function should print out a histogram representing
the number of times each letter occurs in the string. Each occurrence
of a letter should be represented by a star on the specific line for
that letter."""


def histogram(word: str) -> None:
    hist: dict = {}
    for char in range(len(word)):
        letter = word[char]
        if letter not in hist:
            hist[letter] = 0
        hist[letter] += 1
    for key, value in hist.items():
        print(f"{key} {'*' * value}")


def main():
    histogram("statistically")
    # list_words: list[srt] = [
    #     "kazamachi",
    #     "asachan",
    #     "suguru",
    #     "baldomero",
    #     "bakasama",
    #     "python",
    #     "mugiwaratachi",
    #     "parangaricuti",
    # ]
    # for word in list_words:
    #     histogram(word)


if __name__ == "__main__":
    main()
