"""Please write a function named invert(dictionary: dict),
which takes a dictionary as its argument. The dictionary should be
inverted in place so that values become keys and keys become values.
Please write a function named invert(dictionary: dict), which takes
a dictionary as its argument. The dictionary should be inverted in
place so that values become keys and keys become values."""


def invert(dictionary: dict) -> None:
    reversed_dict: dict = {}
    for key, value in dictionary.items():
        reversed_dict[value] = key
    dictionary.clear()
    for key, value in reversed_dict.items():
        dictionary[key] = value


def main() -> None:
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)


if __name__ == "__main__":
    main()
