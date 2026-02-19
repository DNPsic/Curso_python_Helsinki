"""Please write a function named chessboard, which prints out a chessboard
made out of ones and zeroes. The function takes an integer argument, which
specifies the length of the side of the board."""


def chessboard(length: int):
    i = 1
    while i <= length:
        rows = 1
        char = "1"
        if i % 2 == 0:
            char = "0"
        while rows <= length:
            if rows == length:
                print(char)
            else:
                print(char, end="")
            if char == "0":
                char = "1"
            elif char == "1":
                char = "0"
            rows += 1
        i += 1


# Model's solution:
# def chessboard(size):
#     i = 0
#     while i < size:
#         if i % 2 == 0:
#             row = "10"*size
#         else:
#             row = "01"*size
#         # Remove extra characters at the end of the row
#         print(row[0:size])
#         i += 1

if __name__ == "__main__":
    chessboard(3)
