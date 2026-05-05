#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3:
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

     while True:
            try:
                row = int(input(f"Player {player}, enter row (0-2): "))
                col = int(input(f"Player {player}, enter column (0-2): "))

                if row not in range(3) or col not in range(3):
                    print("Coordinates must be between 0 and 2.")
                    continue

                if board[row][col] != " ":
                    print("That spot is already taken!")
                    continue

                break
            except ValueError:
                print("Please enter a valid number.")

    board[row][col] = player

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(f"Player {winner} wins!")
        break

    if board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    player = "O" if player == "X" else "X"

tic_tac_toe()
