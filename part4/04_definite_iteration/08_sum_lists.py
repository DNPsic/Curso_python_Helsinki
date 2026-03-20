"""Please write a function named list_sum which takes
two lists of integers as arguments. The function returns
a new list which contains the sums of the items at each
index in the two original lists. You may assume both lists
have the same number of items."""


def list_sum(first_list: list[int], second_list: list[int]) -> list:
    sum: list[int] = []
    for x in range(len(first_list)):
        sum.append(first_list[x] + second_list[x])
    return sum


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))  # [8, 10, 12]
