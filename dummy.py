from copy import deepcopy
EMPTY, WHITE, BLACK = '.', 'W', 'B'


def free_steps(myboard, fig, need_coordinates=False):
    board = deepcopy(myboard)
    nextlin, free_steps = (1 if fig == 'B' else -1), []
    for lin in range(0, 8):
        for col in range(int(lin % 2 == 0), 8, 2):
            for i in (1, -1):
                try:
                    if board[lin][col] == fig:
                        if board[lin + nextlin][col + i] == '.':
                            board[lin + nextlin][col + i] = '*'
                            free_steps.append([lin + nextlin, col + i])
                        elif board[lin + nextlin][col + i] not in (fig, '*') and board[lin + nextlin * 2][col + i * 2] == '.':
                            board[lin + nextlin * 2][col + i * 2] = '*'
                            free_steps.append([lin + nextlin * 2, col + i * 2])
                        elif board[lin - nextlin][col + i] not in (fig, '*', '.') and board[lin - nextlin * 2][col + i * 2] == '.':
                            board[lin - nextlin * 2][col + i * 2] = '*'
                            free_steps.append([lin - nextlin * 2, col + i * 2])
                except:
                    None
    if need_coordinates:
        return board, free_steps
    else:
        return board


def initial_board():
    board = [[EMPTY for i in range(8)] for j in range(8)]
    black_cells = [[0, 1], [0, 3], [0, 5], [0, 7],
                   [1, 0], [1, 2], [1, 4], [1, 6],
                   [2, 1], [2, 3], [2, 5], [2, 7]]
    white_cells = [[7, 0], [7, 2], [7, 4], [7, 6],
                   [6, 1], [6, 3], [6, 5], [6, 7],
                   [5, 0], [5, 2], [5, 4], [5, 6]]
    for bc in black_cells:
        board[bc[0]][bc[1]] = BLACK
    for wc in white_cells:
        board[wc[0]][wc[1]] = WHITE
    return board


def print_board(board):
    rep = '    ' + ' '.join(list(map(str, [i for i in range(1, 9)]))) + '\n'
    for i in range(1, 9):
        rep += '\n' + str(i) + '   '
        rep += ' '.join(list(map(str, board[i - 1])))
    return rep


# TEST:
board = initial_board()
board[3][2] = 'W'
board[4][3] = 'B'
board[6][5] = 'B'
board[7][4] = '.'
newboard, steps = free_steps(board, 'W', True)
print(print_board(newboard))
print(steps)
# ALL WORK! LIFE IS GOOD!