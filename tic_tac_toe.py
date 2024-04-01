import numpy as np
import random

def dcheck(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
            break
    if win:
        return win

    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win = False
            break
    return win

def check(board, player):
    if dcheck(board, player):
        return True

    for i in range(len(board)):
        wr, wc = True, True
        for j in range(len(board)):
            if board[i, j] != player:
                wr = False
                break
        for j in range(len(board)):
            if board[j, i] != player:
                wc = False
                break
        if wr or wc:
            return True

    return False

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l  # for empty positions

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if check(board, player):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def init():

    return np.zeros((3, 3), dtype=int)

def place(board, player):
    if player == 1:
        while True:
            try:
                current_loc = list(map(int, input("Enter choice (row and column separated by space): ").split()))
                if board[current_loc[0], current_loc[1]] == 0:
                    break
                else:
                    print("Cell already occupied. Try again.")
            except IndexError:
                print("Invalid input. Please enter row and column indices.")
            except ValueError:
                print("Invalid input. Please enter integers.")

    else:
        selection = possibilities(board)
        current_loc = random.choice(selection)

    board[tuple(current_loc)] = player
    return board

def play():
    board, winner = init(), 0
    print(board)

    while winner == 0:
        for player in [1, 2]:
            board = place(board, player)
            print(board)

            winner = evaluate(board)
            if winner != 0:
                break

    if winner == 1:
        print("Player 1 wins!")
    elif winner == 2:
        print("Player 2 wins!")
    elif winner == -1:
        print("It's a draw!")

if __name__ == "__main__":
    play()
