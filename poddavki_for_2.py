board = [[0] * 8]* 8


for pos in range(32 * 33 * 2):
    pos += 1
    if pos % 2 == 0:
        pos //= 2
        first_cell = ['W', pos // 32]
        second_cell = ['B', pos % 32 + 1]
    else:
        pos = (pos + 1) // 2
        first_cell = ['W', pos // 32]
        second_cell = ['W', pos % 32 + 1]
    if first_cell[1] != second_cell[1] and first_cell[1] != 33:
        print(first_cell, second_cell)