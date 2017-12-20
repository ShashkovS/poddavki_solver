table_ro_poddavki = [253] * 32 * 33 * 3


for pos in range(32 * 33 * 3):
    pos_l = pos
    if pos % 2 == 0 and pos % 3 != 0:
        pos //= 3
        first_cell = ['W', pos // 32 + 1]
        second_cell = ['B', pos % 32 + 1]
    elif pos % 3 == 0:
        pos = (pos + 1) // 3
        first_cell = ['B', pos // 32 + 1]
        second_cell = ['B', pos % 32 + 1]
    else:
        pos = (pos + 2) // 3
        first_cell = ['W', pos // 32 + 1]
        second_cell = ['W', pos % 32 + 1]
    if first_cell[1] != second_cell[1] and first_cell[1] != 33 and first_cell[1] != 34:
        print(first_cell, second_cell)
        if first_cell[0] == second_cell[0]:
            table_ro_poddavki[pos_l] = 0 if first_cell[0] == 'W' else 255
print(table_ro_poddavki)