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


# 2d matrix that contains a list of directions for every point.
# The directions point to the next point that is greater.
weighted_inp: List[List[basin_flow_t]] = [[[] for _ in range(len(inp[0]))] for i in range(len(inp))]
for i, line in enumerate(inp):
    for j, x in enumerate(line):
        x_directions: directions_t = []
        directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if x == 9:
            continue
        for d_i, d_j in directions:
            if 0 <= d_i < len(inp) and 0 <= d_j < len(line):
                dir_x = inp[d_i][d_j]
                if dir_x == 9:
                    continue
                if x < dir_x:
                    x_directions.append((d_i, d_j))
        weighted_inp[i][j] = x_directions


# Start with low points and get their basin by adding all connected
# directions. The len of the basin list +1 is the basin size.
sizes = []
for l_i, l_j in low_points:
    stack = weighted_inp[l_i][l_j]
    s_i = 0
    while s_i < len(stack):
        dirs: Tuple[int, int] = stack[s_i]
        d_i, d_j = dirs
        new_dirs = weighted_inp[d_i][d_j]
        for new_dir in new_dirs:
            if new_dir not in stack:
                stack.append(new_dir)
        s_i += 1
    size = len(stack) + 1
    sizes.append(size)


print(reduce(int.__mul__, sorted(sizes, reverse=True)[:3]))

end = time.time()
print("Duration: {:4.3f}s".format(end - start))
