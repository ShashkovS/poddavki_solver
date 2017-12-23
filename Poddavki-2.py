first_cell = []
second_cell = []


def initial_board(colour_1, colour_2, first_cell, second_cell):
    board = [['.' for i in range(8)] for j in range(8)]
    for bc in first_cell:
        board[bc[0]][bc[1]] = colour_1
    for wc in second_cell:
        board[wc[0]][wc[1]] = colour_2
    return board


def print_board(board):
    rep = '    ' + ' '.join(list(map(str, [i for i in range(1, 9)]))) + '\n'
    for i in range(1, 9):
        rep += '\n' + str(i) + '   '
        rep += ' '.join(list(map(str, board[i - 1])))
    return rep


for pos_x_1 in range(8):
    for pos_y_1 in range(8):
        for colour_1 in 'B', 'W':
            for pos_x_2 in range(pos_x_1, 8):
                for pos_y_2 in range(pos_y_1, 8):
                    for colour_2 in 'B', 'W':
                        print(print_board(initial_board(colour_1, colour_2, [[pos_x_1, pos_y_1]], [[pos_x_2, pos_y_2]])))


