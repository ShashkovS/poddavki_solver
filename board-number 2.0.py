def print_board(board):
    rep = '    ' + ' '.join(list(map(str, [i for i in range(1, 9)]))) + '\n'
    for i in range(1, 9): rep += '\n' + str(i) + '   ' + ' '.join(list(map(str, board[i - 1])))
    print(rep)



##########################################################################
##########################################################################


def count_k_symbols(num, k):
    num = str(num)
    if len(num) > k: num = num[:k - len(num)]
    return '0' * (k - len(num)) + num


def num_to_board(num_board):
    num_board, trans = count_k_symbols(num_board, 32), str.maketrans('012345', '.BWbw*')
    board = [['.' for i in range(8)] for j in range(8)]
    for lin in range(0, 8):
        for i, col in enumerate(range((lin + 1) % 2, 8, 2), start=lin * 4):
            board[lin][col] = num_board[i].translate(trans)
    return board


def board_to_num(board):
    num_board, trans = '', str.maketrans('.BWbw*', '012345')
    for lin in range(0, 8):
        for col in range((lin + 1) % 2, 8, 2):
            num_board += board[lin][col].translate(trans)
    return num_board


##########################################################################
##########################################################################

# 0 - .
# 1 - B
# 2 - W
# 3 - b
# 4 - w
# 5 - * (доступные ходы для выбранного цвета фигур)(пока нету такой функции)


# TEST

while True:
    n = input()
    board = num_to_board(n)
    num_board = board_to_num(board)
    print_board(board)
    print(num_board)
    print('\n\n')