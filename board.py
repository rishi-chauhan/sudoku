"""This module is responsible for handling the board"""
from math import sqrt
from typing import List

class Board:
    """This class contains methods that help in manipulating the game board"""
    def __init__(self, entries: List[int]) -> None:
        """initialises the board for the game"""
        self.__board = entries
        self.__dimension=int(sqrt(len(entries)))

    def get_board_dimension(self) -> int:
        """getter function for board dimension"""
        return self.__dimension

    def print_board(self) -> None:
        """Prints board in the current state"""
        print("+" + "---+"*self.__dimension)
        for ind, ele in enumerate(self.__board):
            if (ind+1)%self.__dimension==0:
                print(f"| {ele} |")
                print("+" + "---+"*self.__dimension)
            else:
                print(f"| {ele} ", end="")

    def get_row_board(self) -> List[List[int]]:
        """Returns sudoku board considering rows as major"""
        board = []
        row = []
        for val in self.__board:
            row.append(val)
            if len(row) == self.__dimension:
                board.append(row)
                row = []
        return board

    def get_col_board(self) -> List[List[int]]:
        """Returns sudoku board considering columns as major"""
        board = [[] for i in range(self.__dimension)]
        for index, val in enumerate(self.__board):
            board[index % self.__dimension].append(val)
        return board

    def get_box_board(self) -> List[List[int]]:
        """Returns sudoku board considering box as major"""
        board = [[] for i in range(self.__dimension)]
        box_dimension=int(sqrt(self.__dimension))
        for ind, ele in enumerate(self.__board):
            row=int(ind/self.__dimension)
            col=int(ind%self.__dimension)
            board[(box_dimension*int(row/box_dimension))+int(col/box_dimension)].append(ele)
        return board
