def print_board(board):
    rep = '     ' + ' '.join(list(map(str, [i for i in range(1, 9)]))) + '\n'
    for i in range(1, 9): rep += '\n' + str(i) + '    ' + ' '.join(list(map(str, board[i - 1])))
    return rep



def count_k_symbols(num, k):
    num = str(num)
    if len(num) > k: num = num[:k - len(num)]
    return '0' * (k - len(num)) + num

def num_to_board(num_board):
    num_board = count_k_symbols(num_board, 16)
    board = [['.' for i in range(0, 8)] for j in range(0, 8)]
    for lin in range(0, 8):
        for i, col in enumerate(range(int(lin % 2 == 0), 8, 4),start=lin * 2):
            if num_board[i] in ('1', '4', '7'): board[lin][col + 2] = 'B'
            elif num_board[i] in ('2', '5', '8'): board[lin][col + 2] = 'W'
            if num_board[i] in ('3', '4', '5'): board[lin][col] = 'B'
            elif num_board[i] in ('6', '7', '8'): board[lin][col] = 'W'
    return board

def board_to_num(board):
    num_board = ''
    for lin in range(0, 8):
        for col in range(int(lin % 2 == 0), 8, 4):
            need_continue = True
            for j, a in enumerate(('.', 'B', 'W')):
                for i, b in enumerate(('.', 'B', 'W'), start=j * 3):
                    if board[lin][col] == a and board[lin][col + 2] == b:
                        num_board += str(i)
                        need_continue = False
                        break
                if not need_continue: break
    return count_k_symbols(num_board, 16)


# Каждой цифре, кроме 9, соответствует свои символы ('.', 'B', 'W') на чёрных клетках. (Белые всегда пустуют)
# Всего в номере позиции - 16 цифр: 1 цифра - 2 символа
# Если в номере позиции больше 16 цифр - последние цифры отбрасываются. Хотя можно немного изменить count_k_symbols, чтобы отбрасывались первые цифры
# Если в номере позиции меньше 16 цифр, то в начало добавляются 0 (можно изменить в count_k_symbols, что бы добавлялось в конец). То есть: 508 = 0000000000000508
# Последовательность цифр - последовательность сиволов на чёрных клетках (1стр 2кол + 1стр 4кол, ..., 2стр 1кол + 2стр 3кол, ... ..., 8стр 5кол + 8стр 7кол)
# 0 = ..
# 1 = .B
# 2 = .W
# 3 = B.
# 4 = BB
# 5 = BW
# 6 = W.
# 7 = WB
# 8 = WW
# В коде 9 = 0
# Для примера:
#       Начальная позиция: 4444440000888888
#       Позиция, где W и B стоят по середине: 610000000

while True:
    board = num_to_board(int(input()))
    num_board = board_to_num(board)
    print(print_board(board))
    print(num_board)
    print('\n\n')