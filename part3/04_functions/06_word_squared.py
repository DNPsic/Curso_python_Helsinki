"""Please write a function named squared, which takes a string argument
and an integer argument, and prints out a square of characters
"""


def squared(string: str, number: int) -> None:
    i = 1
    while i <= number:
        i += 1


if __name__ == "__main__":
    squared("ab", 3)
