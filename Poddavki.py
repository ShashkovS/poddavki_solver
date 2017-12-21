table_ro_poddavki = [253] * 32 * 33 * 3
first_step = 1


def swap_pos_num(cell_pos):
    if (first_cell[1] + 3) % 8 == 0:
        first_cell[1] = (first_cell[1] * 2) + 1
    else:
        first_cell[1] *= 2


def check_pos(first_cell, second_cell, num):
    if abs(first_cell[1] - second_cell[1]) == 7:
        if (second_cell[1] - 1) % 8 == 0:
            return num + 1
    elif abs(first_cell - second_cell) == 9:
        if second_cell[1] % 8 == 0:
            return num + 1
    else:
        return check_pos(second_cell, first_cell, num + 1)


for pos in range(32 * 33 * 3):
    pos_l = pos
    pos += 1
    if (pos + 1) % 3 == 0 and pos % 3 != 0:
        pos = (pos + 1) // 3
        first_cell = ['W', pos // 32 + 1]
        second_cell = ['B', pos % 32 + 1]
    elif pos % 3 == 0:
        pos = pos // 3
        first_cell = ['B', pos // 32 + 1]
        second_cell = ['B', pos % 32 + 1]
    elif (pos + 2) % 3 == 0:
        pos = (pos + 2) // 3
        first_cell = ['W', pos // 32 + 1]
        second_cell = ['W', pos % 32 + 1]
    if first_cell[1] != second_cell[1] and first_cell[1] != 33 and first_cell[1] != 34:
        print(first_cell, second_cell)
        if first_cell[0] == second_cell[0]:
            table_ro_poddavki[pos_l] = 0 if first_cell[0] == 'W' else 255
    elif first_cell[1] > 32 or first_cell[1] == second_cell[1]:
        table_ro_poddavki[pos_l] = None
print(table_ro_poddavki)
# на выходе получается таблица оз 0, 255, 253.
# 0 - победа белых 255 - черных
# 253 - простой оценкой определить сложно
