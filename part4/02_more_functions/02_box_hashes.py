"""Please write a function named box_of_hashes, which prints
out a rectangle of hash characters. The function takes one argument,
which specifies the height of the rectangle. The rectangle should be
ten characters wide. The function should call the function line from
the exercise above for the actual printing out. Copy your solution
to that exercise above the code for this exercise. Please don't change
anything in your line function."""


def line(integer: int, string: str):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)


def box_of_hashes(height: int):
    i = 0
    while i < height:
        line(10, "#")
        i += 1


if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
