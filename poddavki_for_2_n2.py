av_coor_pos = []
white_cells = []
black_cells = []
for i in range(8):
    for c in range(0 if i % 2 == 1 else 1, 8, 2):
        av_coor_pos.append(str(i) + str(c))
may_pos = []
for pos_1 in range(len(av_coor_pos)):
    for colour_1 in 'B', 'W':
        for pos_2 in range(pos_1 + 1, len(av_coor_pos)):
            for colour_2 in 'B', 'W':
                may_pos.append([[colour_1, av_coor_pos[pos_1]], [colour_2, av_coor_pos[pos_2]]])


def check_need_eat():
    for wc in white_cells:
        for i in [1, 1], [1, -1], [-1, 1], [-1, -1]:

