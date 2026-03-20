"""Please write a function named shape, which takes four
arguments. The first two parameters specify a triangle,
as above, and the character used to draw it. The first
parameter also specifies the width of a rectangle, while
the third parameter specifies its height. The fourth
parameter specifies the filler character of the rectangle.
The function prints first the triangle, and then the
rectangle below it.
The function should call the function line from the
exercise above for the actual printing out. Copy your
solution to that exercise above the code for this
exercise. Please don't change anything in the line
function."""


def line(integer: int, string: str):
    if string == "":
        print("*" * integer)
    else:
        print(string[0] * integer)


def shape(width, triangle_char, rectangle_size, rectangle_char):
    i = 1
    while i <= width:
        line(i, triangle_char)
        i += 1

    i = 1
    while i <= rectangle_size:
        line(width, rectangle_char)
        i += 1


# TODO Submit to TMC server via VSC.
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    shape(5, "o", 4, ",")
