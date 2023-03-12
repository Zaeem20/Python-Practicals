import os
import numpy as np
import enum


class Game(enum.IntEnum):
    X = 1
    O = -1
    Tie = 2


def printBoard(board):
    states = {-1: "O", 0: " ", 1: "X"}
    print(f" {states[board[1]]} | {states[board[2]]} | {states[board[3]]}")
    print('---+---+---')
    print(f" {states[board[4]]} | {states[board[5]]} | {states[board[6]]}")
    print('---+---+---')
    print(f" {states[board[7]]} | {states[board[8]]} | {states[board[9]]}")
    print("\n")


def spaceIsFree(position):
    if board[position] == 0:
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        os.system('cls')
        printBoard(board)

        winner = checkForWin()
        if winner:
            if winner == Game.X:
                print("Bot wins!")
                exit()
            elif winner == Game.O:
                print("Player wins!")
                exit()
            elif winner == Game.Tie:
                print("Draw")
                exit()
        

        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position: "))
        insertLetter(letter, position)
        return


def checkForWin():
    matrix = np.array_split(list(board.values()), 3)

    # Horizontal Check
    for row in matrix:
        if sum(row) == 3:
            return Game.X  # For X
        elif sum(row) == -3:
            return Game.O # For O
    
    # Vertical Check
    for cell in range(len(matrix)):
        vertical = matrix[0][cell] + matrix[1][cell] + matrix[2][cell]
        if vertical == 3:
            return Game.X  # For X
        elif vertical == -3:
            return Game.O # For O

    # Diagonal Check
    last = 2
    for cell in range(0, 3, 2):
        diagonal = matrix[0][cell]+ matrix[1][1] + matrix[last][2]
        if diagonal == 3:
            return Game.X # For X
        elif diagonal == -3:
            return Game.O  # For O
        last=cell

    if all(cell !=0 for row in matrix for cell in row):
        return Game.Tie # for Tie
    
    return False


def checkDraw():
    for key in board.keys():
        if (board[key] == 0):
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return

def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == 0):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = 0
            # if (score > bestScore):
            bestScore = max(bestScore, score)
            bestMove = key


    insertLetter(bot, bestMove)
    return


def minimax(board: dict, depth, isMaximizing):
    winner = checkForWin()
    if (winner == Game.X):
        return 1
    elif (winner == Game.O):
        return -1
    elif (winner == Game.Tie):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == 0):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = 0
                # if (score > bestScore):
                bestScore = max(bestScore,score)
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == 0):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = 0
                # if (score < bestScore):
                bestScore = min(bestScore, score)
        return bestScore


board= {1: 0, 2: 0, 3: 0,
        4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0}

# printBoard(board)
# print("Computer goes first! Good luck.")
# print("Positions are as follow:")
# print("1, 2, 3 ")
# print("4, 5, 6 ")
# print("7, 8, 9 ")
# print("\n")
player = Game.O
bot = Game.X


# global firstComputerMove
# firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()
    # os.system('cls')
