"""Please write a function named greatest_number, which
takes three arguments. The function returns the greatest
in value of the three.
"""


def greatest_number(a, b, c):
    if c < a > b:
        return a
    if a < b > c:
        return b
    else:
        return c


if __name__ == "__main__":
    print(greatest_number(3, 4, 1))
    print(greatest_number(99, -4, 7))
    print(greatest_number(0, 0, 0))
