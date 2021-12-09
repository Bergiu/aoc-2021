inp = [list(map(int, x)) for x in open("input").read().splitlines()]

low_points = []

for i, line in enumerate(inp):
    for j, x in enumerate(line):
        if i > 0:
            upper = inp[i - 1][j]
            if x >= upper:
                continue
        if j > 0:
            left = inp[i][j - 1]
            if x >= left:
                continue
        if i < len(inp) - 1:
            down = inp[i + 1][j]
            if x >= down:
                continue
        if j < len(line) - 1:
            right = inp[i][j + 1]
            if x >= right:
                continue
        low_points.append((i, j))


print(sum([inp[x][y] + 1 for x, y in low_points]))
