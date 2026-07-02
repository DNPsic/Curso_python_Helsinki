"""Please write a function named double_items(numbers: list),
which takes a list of integers as its argument.
The function should return a new list, which contains all values
from the original list doubled. The function should not change
the original list."""


def double_items(numbers: list) -> list:
    items_doubled: list[int] = []
    for num in numbers:
        items_doubled.append(num * 2)
    return items_doubled


def main() -> None:
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)


if __name__ == "__main__":
    main()
