"""This module is responsible for handling the board"""
from math import sqrt

class Board:
    """This class contains methods that help in manipulating the game board"""
    def __init__(self, entries):
        """initialises the board for the game"""
        self.board = entries
        self.dimension=int(sqrt(len(entries)))

    def print_board(self):
        """Prints board in the current state"""
        print("+" + "---+"*self.dimension)
        for ind, ele in enumerate(self.board):
            if (ind+1)%self.dimension==0:
                print(f"| {ele} |")
                print("+" + "---+"*self.dimension)
            else:
                print(f"| {ele} ", end="")

    def get_row_board(self):
        """Returns sudoku board considering rows as major"""
        board = []
        row = []
        for val in self.board:
            row.append(val)
            if len(row) == self.dimension:
                board.append(row)
                row = []
        return board

    def get_col_board(self):
        """Returns sudoku board considering columns as major"""
        board = [[] for i in range(self.dimension)]
        for index, val in enumerate(self.board):
            board[index % self.dimension].append(val)
        return board

    def get_box_board(self):
        """Returns sudoku board considering box as major"""
        board = [[] for i in range(self.dimension)]
        box_dimension=int(sqrt(self.dimension))
        for ind, ele in enumerate(self.board):
            row=int(ind/self.dimension)
            col=int(ind%self.dimension)
            board[(box_dimension*int(row/box_dimension))+int(col/box_dimension)].append(ele)
        return board
