"""Please write a function named transpose(matrix: list), which takes a two-dimensional
integer array, i.e., a matrix, as its argument. The function should transpose the matrix.
Transposing means essentially flipping the matrix over its diagonal: columns become rows,
and rows become columns.
You may assume the matrix is a square matrix, so it will have an equal number of rows and
columns."""


def transpose(matrix: list[list[int]]) -> None:
    matrix_copy: list[list[int]] = []
    for item in matrix:
        matrix_copy.append(item[:])

    for row in range(len(matrix)):
        for num in range(len(matrix[row])):
            if row != num:
                matrix[row][num] = matrix_copy[num][row]


def main() -> None:
    def print_matrix(matrix: list[list[int]]) -> None:
        for row in matrix:
            print(row)

    matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original matrix:")
    print_matrix(matrix)
    transpose(matrix)
    print("New matrix:")
    print_matrix(matrix)
    matrix2: list[list[int]] = []
    for n in range(20):
        matrix2.append(list())
        for x in range(20):
            matrix2[n].append(x)
    print_matrix(matrix2)
    transpose(matrix2)
    print_matrix(matrix2)


if __name__ == "__main__":
    main()
