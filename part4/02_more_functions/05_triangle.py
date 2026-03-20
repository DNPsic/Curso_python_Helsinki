"""Please write a function named triangle, which draws a triangle
of hashes, and takes one argument. The triangle should be as tall
and as wide as the value of the argument.
The function should call the function line from the exercise above
for the actual printing out. Copy your solution to that exercise
above the code for this exercise. Please don't change anything
in the line function.
"""


def line(integer: int, string: str):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)


def triangle(size):
    i = 0
    while i <= size:
        line(i, "#")
        i += 1


# TODO submit to server via TMC extension in VSC.
if __name__ == "__main__":
    triangle(8)
