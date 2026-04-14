"""Please write a function named sudoku_grid_correct(sudoku: list), which
takes a two-dimensional array representing a sudoku grid as its argument.
The function should use the functions from the three previous exercises to
determine whether the complete sudoku grid is filled in correctly. Copy the
functions from the exercises above into your Python code file for this exercise.
The function should check each of the nine rows, columns and 3 by 3 blocks in
the grid. If all contain each of the numbers 1 to 9 at most once, the function
returns True. If a single one is filled in incorrectly, the function returns False.
The image of a sudoku grid above these exercises has the nine blocks within the
grid indicated with thicker borders. These are the blocks the function should check,
and they begin at the indexes
(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).
"""


def row_correct(sudoku: list[list[int]], row_no: int) -> bool:
    row: list[int] = []
    for num in sudoku[row_no]:
        if num != 0:
            row.append(num)
    for n in row:
        if row.count(n) > 1:
            return False
    return True


def column_correct(sudoku: list[list[int]], column_no: int) -> bool:
    numbers: list[int] = []
    for item in sudoku:
        if item[column_no] > 0 and item[column_no] in numbers:
            return False
        numbers.append(item[column_no])
    return True


def block_correct(sudoku: list[list[int]], row_no: int, column_no: int) -> bool:
    numbers: list[int] = []
    column = column_no
    for i in range(3):
        for col in range(3):
            number = sudoku[row_no][column_no]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
            column_no += 1
        column_no = column
        row_no += 1
    return True


def sudoku_grid_correct(sudoku: list[list[int]]) -> bool:
    blocks: list[list[int]] = [
        [0, 0],
        [0, 3],
        [0, 6],
        [3, 0],
        [3, 3],
        [3, 6],
        [6, 0],
        [6, 3],
        [6, 6],
    ]
    for i in range(len(sudoku)):
        if not row_correct(sudoku=sudoku, row_no=i):
            return False
        if not column_correct(sudoku=sudoku, column_no=i):
            return False
        if not block_correct(
            sudoku=sudoku, row_no=blocks[i][0], column_no=blocks[i][1]
        ):
            # print(
            #     f"Found incorrect block at row {blocks[i][0]} and column {blocks[i][1]}"
            # )
            return False

    # block_correct(sudoku=sudoku, row_no=blocks[0][0], column_no=blocks[0][1])
    # block_correct(sudoku=sudoku, row_no=blocks[1][0], column_no=blocks[1][1])
    # block_correct(sudoku=sudoku, row_no=blocks[2][0], column_no=blocks[2][1])
    # block_correct(sudoku=sudoku, row_no=blocks[3][0], column_no=blocks[3][1])
    # block_correct(sudoku=sudoku, row_no=blocks[4][0], column_no=blocks[4][1])
    # block_correct(sudoku=sudoku, row_no=blocks[5][0], column_no=blocks[5][1])
    # block_correct(sudoku=sudoku, row_no=blocks[6][0], column_no=blocks[6][1])
    # block_correct(sudoku=sudoku, row_no=blocks[7][0], column_no=blocks[7][1])
    # block_correct(sudoku=sudoku, row_no=blocks[8][0], column_no=blocks[8][1])

    return True


def main() -> None:
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    # print("Checking sudoku1...")
    print(sudoku_grid_correct(sudoku1))
    # print("Sudoku1 checked.\n----------")

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]

    # print("Checking sudoku2...")
    print(sudoku_grid_correct(sudoku2))
    # print("Sudoku2 checked.")

    sudoku3 = [
        [2, 9, 5, 0, 8, 4, 7, 1, 3],
        [6, 4, 8, 1, 3, 7, 9, 2, 5],
        [1, 7, 3, 2, 0, 9, 4, 6, 8],
        [8, 6, 0, 3, 4, 1, 2, 5, 7],
        [5, 2, 7, 8, 9, 6, 0, 3, 4],
        [3, 1, 4, 0, 7, 2, 6, 8, 9],
        [7, 5, 0, 9, 2, 8, 1, 4, 0],
        [4, 3, 6, 7, 1, 5, 8, 0, 2],
        [0, 8, 0, 4, 6, 3, 5, 7, 1],
    ]
    print(sudoku_grid_correct(sudoku3))


if __name__ == "__main__":
    main()
