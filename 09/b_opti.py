from typing import List, Tuple, Optional
from functools import reduce
import time

direction_t = Tuple[int, int]
directions_t = List[direction_t]
basin_flow_t = directions_t

inp = [list(map(int, x)) for x in open("input").read().splitlines()]

start = time.time()

low_points = []

for i, line in enumerate(inp):
    for j, x in enumerate(line):
        directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        # check if this is a low_point by comparing to the values of
        # all directions
        lowest = True
        for d_i, d_j in directions:
            if 0 <= d_i < len(inp) and 0 <= d_j < len(line):
                dir_x = inp[d_i][d_j]
                if x >= dir_x:
                    lowest = False
                    break
        if lowest:
            low_points.append((i, j))


def get_dirs(i, j):
    x = inp[i][j]
    directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    if x == 9:
        return []
    for d_i, d_j in directions:
        if 0 <= d_i < len(inp) and 0 <= d_j < len(line):
            dir_x = inp[d_i][d_j]
            if dir_x == 9:
                continue
            if x < dir_x:
                yield (d_i, d_j)


# Start with low points and get their basin by adding all connected
# directions. The len of the basin list +1 is the basin size.
sizes = []
for l_i, l_j in low_points:
    stack = list(get_dirs(l_i, l_j))
    s_i = 0
    while s_i < len(stack):
        dirs: Tuple[int, int] = stack[s_i]
        d_i, d_j = dirs
        for new_dir in get_dirs(d_i, d_j):
            if new_dir not in stack:
                stack.append(new_dir)
        s_i += 1
    size = len(stack) + 1
    sizes.append(size)


print(reduce(int.__mul__, sorted(sizes, reverse=True)[:3]))

end = time.time()
print("Duration: {:4.3f}s".format(end - start))
