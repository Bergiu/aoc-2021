inp = [list(map(int, x)) for x in open("input").read().splitlines()]

low_points = []

for i, line in enumerate(inp):
    for j, x in enumerate(line):
        directions = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1)
        ]
        lowest = True
        for d_i, d_j in directions:
            if 0 <= d_i < len(inp) and 0 <= d_j < len(line):
                dir_x = inp[d_i][d_j]
                if x >= dir_x:
                    lowest = False
                    break
        if lowest:
            low_points.append((i, j))


print(sum([inp[x][y] + 1 for x, y in low_points]))
