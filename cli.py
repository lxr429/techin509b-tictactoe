# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


def print_board(board):
    for row in board:
        print(' '.join([cell if cell is not None else '.' for cell in row]))


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'

    while winner is None:
        print("Current board:")
        print_board(board)
        print(f"Player {current_player}'s turn.")
        while True:
            move = input("Enter your move (row and column, e.g., 1 2): ")
            try:
                row, col = map(int, move.split())
                if board[row - 1][col - 1] is None:
                    board[row - 1][col - 1] = current_player
                    break
                else:
                    print("Invalid move. That position is already taken.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two space-separated numbers.")

        winner = get_winner(board)
        current_player = other_player(current_player)

    print("Final board:")
    print_board(board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")
