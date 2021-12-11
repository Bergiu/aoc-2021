from itertools import product
import numpy as np
filename = "input"
rounds = 100

inp = [list(map(int, x)) for x in open(filename).read().splitlines()]
data = []
for i, line in enumerate(inp):
    for j, x in enumerate(line):
        data.append([i, j, x])


def print_data():
    for i in range(10):
        for j in range(10):
            print(data[i * 10 + j][2], end="")
        print()
    print()

flash = 0
round = 0
while True:
    new_flashes = 0
    # increase
    for item in data:
        item[2] += 1
    # flash
    find_9 = list(filter(lambda part: part[2] > 9, data))
    for item in find_9:
        i, j, _ = item
        dirs = np.add(list(set(product(*[[-1, 0, 1]] * 2)) - set([(0, 0)])), (i, j))
        adjacents = [data[x * 10 + y] for x, y in dirs if 0 <= x < 10 and 0 <= y < 10]
        for adjacent in adjacents:
            if adjacent[2] == 9:
                adjacent[2] = 0
                find_9.append(adjacent)
            elif adjacent[2] != 0:
                adjacent[2] += 1
        item[2] = 0
        flash += 1
        new_flashes += 1
    if new_flashes >= 100:
        print("Rounds", round + 1)
        break
    round += 1
