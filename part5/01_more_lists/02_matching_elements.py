"""Please write a function named
count_matching_elements(my_matrix: list, element: int),
which takes a two-dimensional array of integers and a single
integer value as its arguments. The function then counts
how many elements within the matrix match the argument value."""


def count_matching_elements(my_matrix: list[list[int]], element: int) -> int:
    result: int = 0
    for item in range(len(my_matrix)):
        for number in range(len(my_matrix[item])):
            if my_matrix[item][number] == element:
                result += 1

    return result


def main():
    # m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
    print(count_matching_elements(m, 2))


if __name__ == "__main__":
    main()
