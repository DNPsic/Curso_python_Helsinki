"""Please write a function named everything_reversed, which
takes a list of strings as its argument. The function returns
a new list with all of the items on the original list reversed.
Also the order of items should be reversed on the new list."""


def everything_reversed(words: list[str]) -> list[str]:
    new_list: list[str] = []
    for w in words:
        new_list.append(w[::-1])
    return new_list[::-1]


if __name__ == "__main__":
    my_list: list[str] = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
