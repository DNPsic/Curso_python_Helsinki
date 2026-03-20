"""Please write a function named distinct_numbers, which
takes a list of integers as its argument. The function
returns a new list containing the numbers from the
original list in order of magnitude, and so that each
distinct number is present only once."""


def distinct_numbers(numbers: list[int]) -> list:
    distinct_numbers: list[int] = []
    for n in sorted(numbers):
        if n not in distinct_numbers:
            distinct_numbers.append(n)
    return distinct_numbers


if __name__ == "__main__":
    my_list: list[int] = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))
