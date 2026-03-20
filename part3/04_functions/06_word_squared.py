"""Please write a function named squared, which takes a string argument
and an integer argument, and prints out a square of characters
"""


# Write your solution here
def squared(word, length):
    word *= length * length
    i = 1
    start = 0
    end = length
    while i <= length:
        print(word[start:end])
        start += length
        end += length
        i += 1


if __name__ == "__main__":
    squared("ab", 3)
