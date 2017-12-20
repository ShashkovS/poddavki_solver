for i in range(32):
    for c in 'W', 'B':
        for n in range(32):
            for m in 'W', 'B':
                if i != n:
                    print([c, i], [m, n])