white_cells = []
black_cells = []
white_kings = []
black_kings = []
white_cells.append(list(map(int, input().split())))
black_cells.append(list(map(int, input().split())))


def initial_board():
    board = [['.' for i in range(8)] for j in range(8)]
    for bc in black_cells:
        board[bc[0]][bc[1]] = 'B'
    for wc in white_cells:
        board[wc[0]][wc[1]] = 'W'
    return board


def print_board(board):
    rep = '    ' + ' '.join(list(map(str, [i for i in range(1, 9)]))) + '\n'
    for i in range(1, 9):
        rep += '\n' + str(i) + '   '
        rep += ' '.join(list(map(str, board[i - 1])))
    return rep


print(print_board(initial_board()))