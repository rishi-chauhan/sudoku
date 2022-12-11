"""This module is responsible for handling the board"""
from math import sqrt
from typing import List

CORRECT_PATTERN = set(range(1,10))
DIMENSION = 9

def print_board(board) -> None:
    """Prints board in the current state"""
    print("+" + "---+"*DIMENSION)
    for ind, ele in enumerate(board):
        if (ind+1)%DIMENSION==0:
            print(f"| {ele} |")
            print("+" + "---+"*DIMENSION)
        else:
            print(f"| {ele} ", end="")

def get_row_board(board) -> List[List[int]]:
    """Returns sudoku board considering rows as major"""
    row_board = []
    row = []
    for val in board:
        row.append(val)
        if len(row) == DIMENSION:
            row_board.append(row)
            row = []
    return board

def get_col_board(board) -> List[List[int]]:
    """Returns sudoku board considering columns as major"""
    board = [[] for i in range(DIMENSION)]
    for index, val in enumerate(board):
        board[index % DIMENSION].append(val)
    return board

def get_box_board(board) -> List[List[int]]:
    """Returns sudoku board considering box as major"""
    board = [[] for i in range(DIMENSION)]
    box_dimension=int(sqrt(DIMENSION))
    for ind, ele in enumerate(board):
        row=int(ind/DIMENSION)
        col=int(ind%DIMENSION)
        board[(box_dimension*int(row/box_dimension))+int(col/box_dimension)].append(ele)
    return board

def check_if_correct(board):
    """checks if array of elements is solved"""
    for ele in board:
        ele.sort()
        if ele == CORRECT_PATTERN:
            return True
    return False
