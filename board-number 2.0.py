def print_board(board, step):
    step = 'B' if step == '1' else 'W'
    rep = '    ' + ' '.join(list(map(str, [i for i in range(1, 9)]))) + '\n'
    for i in range(1, 9): rep += '\n' + str(i) + '   ' + ' '.join(list(map(str, board[i - 1])))
    print('Ход', step)
    print(rep)



##########################################################################
##########################################################################


def count_k_symbols(num, k):
    num = str(num)
    if len(num) > k: num = num[:k - len(num)]
    return '0' * (k - len(num)) + num


def num_to_board(num_board):
    num_board, trans = count_k_symbols(num_board, 33), str.maketrans('012345', '.BWbw*')
    num_board, step = num_board[:-1], num_board[-1]
    print(num_board)
    board = [['.' for i in range(8)] for j in range(8)]
    for lin in range(0, 8):
        for i, col in enumerate(range((lin + 1) % 2, 8, 2), start=lin * 4):
            board[lin][col] = num_board[i].translate(trans)
    print(board)
    return board, step


def board_to_num(board, step='1'):
    num_board, trans = '', str.maketrans('.BWbw*', '012345')
    for lin in range(0, 8):
        for col in range((lin + 1) % 2, 8, 2):
            print(board)
            num_board += board[lin][col].translate(trans)
    return num_board + step


##########################################################################
##########################################################################

# 0 - .
# 1 - B
# 2 - W
# 3 - b
# 4 - w
# 5 - * (доступные ходы для выбранного цвета фигур)(пока нету такой функции)
# Последняя цифра - чей ход (1 - BLACK, 2 - WHITE)



# TEST

while True:
    n = input() + '1'
    board, step = num_to_board(n)
    num_board = board_to_num(board)
    print_board(board, step)
    print(num_board)
    print('\n\n')