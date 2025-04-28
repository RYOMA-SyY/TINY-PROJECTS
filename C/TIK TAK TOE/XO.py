import numpy as np

def show(board):
    print(f"""
     {board['1']} | {board['2']} | {board['3']} 
    ---|---|---
     {board['4']} | {board['5']} | {board['6']} 
    ---|---|---
     {board['7']} | {board['8']} | {board['9']} 
    """)

def check_win(board, player):
    win_combinations = [
        ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # Rows
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Columns
        ['1', '5', '9'], ['3', '5', '7']                   # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

def main():
    board = {str(i): ' ' for i in range(1, 10)}
    turn = 'X'
    print("Welcome to Tic-Tac-Toe!")

    for _ in range(9):  # Maximum of 9 moves
        show(board)
        move = input(f"Player {turn}, choose a position (1-9): ")
        if move not in board or board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = turn
        if check_win(board, turn):
            show(board)
            print(f"Player {turn} wins!")
            return
        turn = 'O' if turn == 'X' else 'X'

    show(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()