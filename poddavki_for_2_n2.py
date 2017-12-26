white_cells = list()
for i in range(int(input())):
    white_cells.append(list(map(int, input().split())))
black_cells = list()
for c in range(int(input())):
    black_cells.append(list(map(int, input().split())))
now_step = int(input())


def check_need_eat():
    res_check = list()
    if now_step == 1:
        for wc in white_cells:
            for i in [1, 1], [1, -1], [-1, 1], [-1, -1]:
                if [wc[0] + i[0], wc[1] + i[1]] in black_cells:
                    if wc[0] + 2 * i[0] >= 0 and wc[0] + 2 * i[0] <= 7 and wc[1] + 2 * i[1] >= 0 and wc[1] + 2 * i[1] <= 7 and [wc[0] + 2 * i[0], wc[1] + 2 * i[1]] not in black_cells + white_cells:
                        res_check.append('W ' + ' '.join(map(str, wc)) + ' to ' + str(wc[0] + 2 * i[0]) + ' ' + str(wc[1] + 2 * i[1]) + ' eating ' + 'B ' + str(wc[0] + i[0]) + ' ' + str(wc[1] + i[1]))
    elif now_step == 2:
        for bc in black_cells:
            for l in [1, 1], [1, -1], [-1, 1], [-1, -1]:
                if [bc[0] + l[0], bc[1] + l[1]] in white_cells:
                    if bc[0] + 2 * l[0] >= 0 and bc[0] + 2 * l[0] <= 7 and bc[1] + 2 * l[1] >= 0 and bc[1] + 2 * l[1] <= 7 and [bc[0] + 2 * l[0], bc[1] + 2 * l[1]] not in white_cells + black_cells:
                        res_check.append('B ' + ' '.join(map(str, bc)) + ' to ' + str(bc[0] + 2 * l[0]) + ' ' + str(bc[1] + 2 * l[1]) + ' eating ' + 'W ' + str(bc[0] + l[0]) + ' ' + str(bc[1] + l[1]))
    return res_check


def check_av_steps():
    res_check = check_need_eat()
    if len(res_check) != 0:
        return res_check
    else:
        print('Ничего срубить нельзя')
        av_steps = list()
        if now_step == 1:
            for wc in white_cells:
                for i in [1, 1], [1, -1], [-1, 1], [-1, -1]:
                    if [wc[0] + i[0], wc[1] + i[1]] not in black_cells + white_cells and wc[0] + i[0] <= 7 and wc[0] + i[0] >= 0 and wc[1] + i[1] <= 7 and wc[1] + i[1] >= 0:
                        av_steps.append('W ' + ' '.join(map(str, wc)) + ' to ' + str(wc[0] + i[0]) + ' ' + str(wc[1] + i[1]))
        if now_step == 2:
            for bc in black_cells:
                for i in [1, 1], [1, -1], [-1, 1], [-1, -1]:
                    if [bc[0] + i[0], bc[1] + i[1]] not in black_cells + white_cells and bc[0] + i[0] <= 7 and bc[0] + i[0] >= 0 and bc[1] + i[1] <= 7 and bc[1] + i[1] >= 0:
                        av_steps.append('B ' + ' '.join(map(str, bc)) + ' to ' + str(bc[0] + i[0]) + ' ' + str(bc[1] + i[1]))
        return av_steps


def initial_board(white_cells, black_cells):
    board = [['.' for n in range(8)] for j in range(8)]
    if len(black_cells) != 0:
        for bc in black_cells:
            board[bc[0] - 1][bc[1]] = 'B'
    if len(white_cells) != 0:
        for wc in white_cells:
            board[wc[0] - 1][wc[1]] = 'W'
    return board


def print_board(board):
    rep = '    ' + ' '.join(list(map(str, [i for i in range(8)]))) + '\n'
    for i in range(8):
        rep += '\n' + str(i) + '   '
        rep += ' '.join(list(map(str, board[i - 1])))
    return rep


print(print_board(initial_board(white_cells, black_cells)))
if len(black_cells) == 0:
    print('Чёрные выиграли')
elif len(white_cells) == 0:
    print('Белые выиграли')
else:
    print(check_av_steps())
