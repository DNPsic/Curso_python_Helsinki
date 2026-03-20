"""Please write a function named square, which prints out a square
of characters, and takes two arguments. The first parameter specifies
the length of the side of the square. The second parameter specifies
the character used to draw the square.
The function should call the function line from the exercise above
for the actual printing out. Copy your solution to that exercise above
the code for this exercise. Please don't change anything in the line function.
"""


def line(integer: int, string: str):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)


def square(size: int, character: str):
    i = 0
    while i < size:
        line(size, character)
        i += 1


if __name__ == "__main__":
    square(4, "*")
