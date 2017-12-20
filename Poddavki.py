from copy import deepcopy

EMPTY,    WHITE, BLACK = '.', 'W', 'B'


def free_steps(my_board, fig):
    board = deepcopy(my_board)
    free_steps = []
    nextlin = 1 if fig == 'B' else -1
    for lin in range(0, 7):
        for col in range(int(lin % 2 == 0), 7, 2):
            if board[lin][col] == fig:
                for i in (-1, 1):
                    try:
                        if board[lin + nextlin][col + i] == '.':
                            board[lin + nextlin][col + i] = '*'
                            free_steps.append([lin + nextlin, col + i])
                        elif board[lin + nextlin][col + i] != fig:
                            try:
                                if board[lin + nextlin * 2][col + i * 2] == '.':
                                    board[lin + nextlin * 2][col + i * 2] = '*'
                                    free_steps.append([lin + nextlin * 2, col + i * 2])
                                if board[lin + nextlin * 2][col - i]:
                            except:
                                None

                    except:
                        None

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


print(print_board(free_steps(initial_board(), 'B')))