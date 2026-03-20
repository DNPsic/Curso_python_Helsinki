"""Please write a function named range_of_list, which takes
a list of integers as an argument. The function returns the
difference between the smallest and the largest value in the
list."""


def range_of_list(numbers: list[int]) -> int:
    numbers.sort()
    return numbers[-1] - numbers[0]


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)
