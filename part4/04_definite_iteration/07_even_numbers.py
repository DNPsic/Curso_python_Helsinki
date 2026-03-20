"""Please write a function named even_numbers, which
takes a list of integers as an argument. The function
returns a new list containing the even numbers from
the original list."""


def even_numbers(numbers: list[int]) -> list:
    even_numbers: list = []
    for x in numbers:
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
