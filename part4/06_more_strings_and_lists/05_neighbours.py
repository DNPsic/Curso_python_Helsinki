"""Given a list of integers, let's decide that two consecutive
items in the list are neighbours if their difference is 1. So,
items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours,
which looks for the longest series of neighbours within the
list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list
of neighbours would be [5, 4, 3, 4], with a length of 4."""


def longest_series_of_neighbours(numbers: list[int]) -> int:
    result: int = 0
    consecutive_count: int = 0
    index: int = 0
    for number in numbers[: len(numbers) - 1]:
        neighbour = numbers[index + 1]
        # print(
        #     f"Current result: {result}\nCurrent consecutive_count: {consecutive_count}"
        # )
        # print(f"Comparing {number} with {numbers[index + 1]}")
        if number + 1 == neighbour or number - 1 == neighbour:
            # print(f"Number {number} is {neighbour}'s neighbour")
            consecutive_count += 1
            # print(f"Consecutive count: {consecutive_count} {'*':>5}\n")
            if result < consecutive_count:
                result = consecutive_count
        else:
            consecutive_count = 0
            if consecutive_count < 0:
                consecutive_count = 0
            # print(f"Number {number} is NOT {neighbour}'neighbour")
            # print(f"Consecutive count: {consecutive_count}\n")
        index += 1
    return result + 1


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
    my_list2 = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list2))
