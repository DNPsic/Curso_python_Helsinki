"""Please write a function named length which takes a list
as its argument and returns the length of the list."""


def length(arg_list: list) -> int:
    return len(arg_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    result = length(my_list)
    print("The length is: ", result)
