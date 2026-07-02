"""In this exercise we will complete two more functions
for the sudoku project from the previous section:
print_sudoku and add_number.
The function print_sudoku(sudoku: list) takes a two-dimensional
array representing a sudoku grid as its argument.
The function
add_number(sudoku: list, row_no: int, column_no: int, number:int)
takes a two-dimensional array representing a sudoku grid, two
integers referring to the row and column indexes of a single
square, and a single digit between 1 and 9, as its arguments.
The function should add the digit to the specified location
in the grid."""


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


def add_number(
    sudoku: list[list[int]], row_no: int, column_no: int, number: int
) -> None:
    sudoku[row_no][column_no] = number


def main() -> None:
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
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)


if __name__ == "__main__":
    main()

# Model's solution:
# def print_sudoku(sudoku: list):
#     r = 0
#     for row in sudoku:
#         s = 0
#         for character in row:
#             s += 1
#             if character == 0:
#                 character = "_"
#             m = f"{character} "
#             if s%3 == 0 and s < 8:
#                 m += " "
#             print(m, end="")
#
#         print()
#         r += 1
#         if r%3 == 0 and r < 8:
#             print()
#
# def add_number(sudoku: list, row_no: int, column_no: int, number: int):
#     sudoku[row_no][column_no] = number
