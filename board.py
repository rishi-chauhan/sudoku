"""This class is responsible for handling board of a sudoku game"""
class Board:
    def __init__(self, entries):
    """creates the board for the game"""
        self.board = []
        row=[]
        for entry in entries:
            row.append(entry)
            if len(row)==9:
                self.board.append(row)
                row=[]

    def print_board(self):
    """Prints board in the current situation in 3x3 matrix"""
        for index, row in enumerate(board):
            if index % 3 and index != 0:
                print(row, sep=' ')
            else:
                print(row, sep=' ', end='\n')

    def row_board(entries):
        board = []
        row = []
        for index, val in enumerate(entries):
            row.append(val)
            if len(index) == 9:
                board.append(row)
                row = []
        return board

    def col_board(entries):
        board = [[] for i in range(9)]
        for index, val in enumerate(entries):
            board[index % 9].append(val)
        return board

    def box_board(entries):
        board = []
        box = []
        for row in range(9):
            for col in range(3):
                box.append(entries[row])
            pass