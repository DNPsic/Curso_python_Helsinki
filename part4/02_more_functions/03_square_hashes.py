"""Please write a function named square_of_hashes, which draws a square
of hash characters. The function takes one argument, which determines
the length of the side of the square. The function should call the function
line from the exercise above for the actual printing out. Copy your solution
to that exercise above the code for this exercise. Please don't change anything
in the line function."""


def line(integer: int, string: str):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)


def square_of_hashes(length: int):
    i = 0
    while i < length:
        line(length, "#")
        i += 1


if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
