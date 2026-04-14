"""Please write a function named who_won(game_board: list), which
takes a two-dimensional array as its argument. The array consists
of integer values, which represent the following situations:
0: empty square
1: player 1 game piece
2: player 2 game piece
The scoring rules of Go can be quite complex, but in this exercise
it is enough to compare the number of pieces each player has on the
game board. Also, the size of the game board is not limited.

The function should return the value 1 if player 1 won, and the value
2 if player 2 won. If both players have the same number of pieces on
the board, the function should return the value 0."""


def who_won(game_board: list[list[int]]) -> int:
    player1: int = 0
    player2: int = 0
    for item in game_board:
        for piece in item:
            if piece == 1:
                player1 += 1
            if piece == 2:
                player2 += 1
    print("Final scores")
    print(f"Player 1:{player1}\nPlayer 2: {player2}")
    if player1 > player2:
        return 1
    elif player1 < player2:
        return 2
    else:
        return 0


def main():
    game: list[list[int]] = [
        [1, 0, 1, 2, 0],
        [0, 2, 2, 1, 0],
        [2, 1, 0, 0, 1],
        [1, 1, 2, 2, 0],
    ]
    print(who_won(game))


if __name__ == "__main__":
    main()
