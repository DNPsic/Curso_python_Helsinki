"""Please write a function named mean, which takes three integer arguments.
The function should print out the arithmetic mean of the three arguments."""


def mean(int1: int, int2: int, int3: int):
    mean = (int1 + int2 + int3) / 3
    print(mean)


if __name__ == "__main__":
    mean(3, 5, 7)
