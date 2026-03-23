"""The Python string method isupper() returns True if a string
consists of only uppercase characters.
Please use the isupper method to write a function named ro_shouting,
which takes a list of strings as an argument. The function returns
a new list, containing only those items from the original which
do not consist of solely uppercase characters."""


def no_shouting(strings: list[str]) -> list[str]:
    new_list: list[str] = []
    for item in strings:
        if not item.isupper():
            new_list.append(item)
    return new_list
    # return [item for item in strings if not item.isupper()]


if __name__ == "__main__":
    my_list = [
        "ABC",
        "def",
        "UPPER",
        "ANOTHERUPPER",
        "lower",
        "another lower",
        "Capitalized",
    ]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
