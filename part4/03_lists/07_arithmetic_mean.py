"""Please write a function named mean, which takes a list
of integers as an argument. The function returns the
arithmetic mean of the values in the list."""


def mean(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)
