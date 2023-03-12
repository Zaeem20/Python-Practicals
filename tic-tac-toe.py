import enum
import copy
import random
import numpy as np
import os, time
import platform
from colorama import just_fix_windows_console
from typing import List, Tuple, Literal



class GameState(enum.IntEnum):
    X = 1  # Player
    O = -1 # player2 = ai or pvp
    DRAW = 2  # Draw state


class TicTacToe:
    """ Tic-Tac-Toe with multiplayer mode\n
    Written by Zaeem Durani
    """
    def __init__(self, mode: Literal['ai', 'pvp']='ai', level=0) -> None:
        self.available_modes = {'pvp': 1, 'ai': 0}
        self.board = np.zeros((3,3))
        self.player2 = self.available_modes.get(mode)
        self.level = level if not self.player2 else None
        self.current_setting = (mode, self.level)

    @classmethod
    def restart(cls, mode, level):
        return cls(mode, level)

    def update_board(self, value: int, cord=()):
        if cord:
            if self.isempty(self.board, cord):
                self.board[cord[0]][cord[1]]=value
                return True
            return False

    def printBoard(self, board):
        state = {1: '\033[1;31mX\033[0m', -1: '\033[1;92mO\033[0m', 0: ' '}   # adding colors

        print(f'  {state[board[0][0]]} \033[1;36m|\033[0m {state[board[0][1]]} \033[1;36m|\033[0m {state[board[0][2]]}')
        print('\033[1;36m----+---+----\033[0m')
        print(f'  {state[board[1][0]]} \033[1;36m|\033[0m {state[board[1][1]]} \033[1;36m|\033[0m {state[board[1][2]]}')
        print('\033[1;36m----+---+----\033[0m')
        print(f'  {state[board[2][0]]} \033[1;36m|\033[0m {state[board[2][1]]} \033[1;36m|\033[0m {state[board[2][2]]}')

    def isempty(self, board, cor: tuple):
        if board[cor[0]][cor[1]] == 0:
            return True
        return False

    def check_board_winner(self, board: List[list]):
        # Horizontal Check 
        for rows in board:
            if sum(rows) == 3:
                return GameState.X
            elif sum(rows) == -3:
                return GameState.O

        # Vertical Check
        for cell in range(len(board)):
            value = board[0][cell] + board[1][cell] + board[2][cell]
            if value == 3:
                return GameState.X   # for X's Win
            elif value == -3:
                return GameState.O  # for O's Win

        # Diagonals Check
        last = 2
        for i in range(0, 3, 2):
            diagonal = board[i][0] + board[1][1] + board[last][2]
            if diagonal == 3:
                return GameState.X
            elif diagonal == -3:
                return GameState.O
            last = i

        if all(i != 0 for row in board for i in row):
            return GameState.DRAW    # For Tie
        return False

    def minimax(self, board, isMaximizing) -> Tuple[int, tuple]:
        state = self.check_board_winner(board)
        if state == GameState.X:
            return 1, None
        if state == GameState.O:
            return -1, None
        elif state == GameState.DRAW:
            return 0, None

        if isMaximizing:
            max_val = -100
            bestMove = None
            empty_cells = self.get_empty_cells(board)

            for (row, column) in empty_cells:
                temp_board = copy.deepcopy(board)
                temp_board[row][column] = GameState.X
                score = self.minimax(temp_board, False)[0]
                if score > max_val:
                    max_val = score
                    bestMove = (row, column)

            return max_val, bestMove
        
        else:
            min_val = 100
            bestMove = None
            empty_cells = self.get_empty_cells(board)

            for (row, column) in empty_cells:
                temp_board = copy.deepcopy(board)
                temp_board[row][column] = GameState.O
                score = self.minimax(temp_board, True)[0]
                if score < min_val:
                    min_val = score
                    bestMove = (row, column)

            return min_val, bestMove


    def _pos_to_cord(self, position) -> tuple:
        if position > 9:
            raise ValueError
        row = (position-1)//3
        col = (position-1)%3
        return (row, col)

    def get_empty_cells(self, board: List[list]) -> List[tuple]:
        """ Get cordinates of all available empty cells in board """
        empty = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    empty.append((row, col))
        return empty


    def ai_player(self, board, level=0):
        """ Play against AI player """
        if not level:
            bestMove = random.choice(self.get_empty_cells(board))
        else:
            score, bestMove = self.minimax(board, False)
        # print(bestMove) For Debugging
        self.update_board(-1, bestMove)
        return


    def start(self):
        """ Mainloop of Game """
        turn = 1    # 1 for X, 0 for O
        while True:
            os.system('cls')
            self.printBoard(self.board)
            if turn:
                try:
                    print("\n\033[1;31mIt's X turn\033[0m")
                    position = int(input("Enter the Position from 1-9:"))
                    updated = self.update_board(1, self._pos_to_cord(position))
                    if not updated:
                        print("Can't update values, Try Again!!!")
                        time.sleep(1.5)
                        continue
                except (ValueError, IndexError):
                        print('\033[1;31mPlease Enter Correct coordinates\033[0m')
                        time.sleep(2.5)
                        continue
            else:
                if not self.player2:
                    self.ai_player(self.board, self.level)
                else:
                    try:
                        print("\n\033[1;92mIt's O turn\033[0m")
                        position = int(input("Enter the Position from 1-9:"))
                        updated = self.update_board(-1, self._pos_to_cord(position))
                        if not updated:
                            print("Can't update values, Try Again!!!")
                            time.sleep(1.5)
                            continue
                    except (ValueError, IndexError):
                        print('\033[1;31mPlease Enter Correct coordinates\033[0m')
                        time.sleep(2.5)
                        continue

            winner = self.check_board_winner(self.board)
            if winner == 1:
                os.system('cls')
                self.printBoard(self.board)
                print("\nHurray!, Player \033[1;31mX\033[0m is the winner")
                break
            elif winner == -1:
                os.system('cls')
                self.printBoard(self.board)
                print("\nHurray!, Player \033[1;92mO\033[0m is the winner")
                break
            elif winner == 2:
                os.system('cls')
                self.printBoard(self.board)
                print('\nMatch Draw!!! Nice try kiddo...')
                break
            turn = int(not turn)
        restart = input("Would you like to restart Again (Y/n):").lower()
        if restart == 'y':
            new_game = TicTacToe.restart(*self.current_setting)
            new_game.start()
        else:
            print("\033[1;31mGood Bye!!!\033[0m")

if __name__ == '__main__':
    try:
        if platform.system() == 'Windows':
            just_fix_windows_console()
        mode = None
        level = 0
        while not mode:
            selected_mode = input("Select mode [ai/pvp]:").lower()
            if selected_mode == 'ai':
                difficulty = input('Select difficulty level [Easy/Insane]:').lower()
                if difficulty == 'insane':
                    level = 1
                mode = 'ai'
            elif selected_mode == 'pvp':
                mode = 'pvp'
            else:
                print("Only select one of available modes: [ai/pvp]. Try Again!!!")

        game = TicTacToe(mode=mode, level=level)
        game.start()
    except KeyboardInterrupt:
        print('\n\033[1;92m[\033[0m+\033[1;92m]\033[0m\033[1;31m Exitting, Good Bye!!!\033[0m')