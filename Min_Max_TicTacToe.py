import numpy as np
import random

player, opponent = 1, 2

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
        if len(possibilities(board)) == 9:
            current_loc = random.choice(possibilities(board))
        else:
            bestMove = findBestMove(board)
            current_loc = bestMove

    board[tuple(current_loc)] = player
    return board

def isMovesLeft(board) :
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == 0) :
                return True
    return False

def minimax(board, depth, isMax) :
    score = evaluate(board)

    if (score == 1) :
        return score

    if (score == -1) :
        return score

    if (isMovesLeft(board) == False) :
        return 0

    if (isMax) :
        best = -1000

        for i in range(3) :
            for j in range(3) :
                if (board[i][j] == 0) :
                    board[i][j] = player

                    best = max( best, minimax(board, depth + 1, not isMax) )

                    board[i][j] = 0
        return best

    else :
        best = 1000

        for i in range(3) :
            for j in range(3) :
                if (board[i][j] == 0) :
                    board[i][j] = opponent

                    best = min(best, minimax(board, depth + 1, not isMax))

                    board[i][j] = 0
        return best

def findBestMove(board) :
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == 0) :
                board[i][j] = player

                moveVal = minimax(board, 0, False)

                board[i][j] = 0

                if (moveVal > bestVal) :
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

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