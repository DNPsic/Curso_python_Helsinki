"""This is the very last sudoku task. This time we will create a slightly
different version of the function for adding new numbers to the grid.
The function copy_and_add(sudoku: list, row_no: int, column_no: int,
number: int) takes a two-dimensional array representing a sudoku grid,
two integers referring to the row and column indexes of a single
square, and a single digit between 1 and 9, as its arguments. The
function should return a copy of the original grid with the new digit
added in the correct location. The function should not change the
original grid received as a parameter.
The print_sudoku function from the previous exercise could be useful
for testing, and it is used in the example below:"""


# NOTE:
# My solution takes up to >200 steps in python tutor
# while the model's just takes 36, which is a much less effort.
def copy_and_add(
    sudoku: list[list[int]], row_no: int, column_no: int, number: int
) -> list:
    sudoku_copy: list[list[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] != 0:
                sudoku_copy[row][col] = sudoku[row][col]
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy


def main() -> None:
    def print_sudoku(sudoku: list[list[int]]) -> None:
        count_rows: int = 0
        for item in range(len(sudoku)):
            for num in range(0, 9, 3):
                row: list[int] = sudoku[item][num : num + 3]
                # print(row, " ", end="")
                for digit in row:
                    if digit == 0:
                        print("_ ", end="")
                    else:
                        print(digit, "", end="")
                print(" ", end="")
            count_rows += 1
            if count_rows == 3 or count_rows == 6:
                print()
            print()

    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)


if __name__ == "__main__":
    main()

# Model's solution
# def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
#    new_list = []
#    for r in sudoku:
#        new_list.append(r[:])
#
#    new_list[row_no][column_no] = number
#    return new_list
