"""ENTRIES contains the values of each cell"""
ENTRIES = [None, None, None, 2, 6, None, 7, None, 1, 6, 8, None, None, 7, None, None, 9, None, 1,
           9, None, None, None, 4, 5, None, None, 8, 2, None, 1, None, None, None, 4, None, None,
           None, 4, 6, None, 2, 9, None, None, None, 5, None, None, None, 3, None, 2, 8, None,
           None, 9, 3, None, None, None, 7, 4, None, 4, None, None, 5, None, None, 3, 6, 7,
           None, 3, None, 1, 8, None, None, None]
TOTAL_SUM = 45

def print_board(board):
    for index, row in enumerate(board):
        if index % 3 and index != 0:
            print(row, sep=' ')
        else:
            print(row, sep=' ', end='\n')

def create_board(entries):
    board = []
    chota_row = []
    bada_row = []
    for i in entries:
        chota_row.append(i)
        if len(chota_row) == 3:
            bada_row.append(chota_row)
            chota_row = []
        if len(bada_row) == 3:
            board.append(bada_row)
            bada_row = []
    return board

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

BOARD = create_board(ENTRIES)
print_board(row_board(ENTRIES))
print("\n")
print_board(col_board(ENTRIES))
print("\n")
print_board(BOARD)
