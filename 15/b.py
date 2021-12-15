from dataclasses import dataclass, field
from typing import Any, List
from pprint import pprint
from operator import itemgetter
import heapq

data_raw = open("input").read().splitlines()
data_expanded_x: List[str] = []
for line in data_raw:
    tmp: List[List[int]] = [[] for _ in range(5)]
    for character in line:
        for i in range(5):
            number = int(character) + i
            if number > 9:
                number -= 9
            tmp[i].append(number)
    data_expanded_x.append("".join(["".join(map(str, part)) for part in tmp]))
data_expanded: List[str] = []
for i in range(5):
    for line in data_expanded_x:
        tmp_line: List[str] = []
        for character in line:
            number = int(character) + i
            if number > 9:
                number -= 9
            tmp_line.append(str(number))
        data_expanded.append("".join(tmp_line))


data = [
    [None, *[
        {'val': int(val), 'finished': False, 'cost': float('inf'), 'route': []}
        for val in x
    ], None]
    for x in data_expanded]
data.insert(0, [None] * len(data[0]))
data.append([None] * len(data[0]))


# for line in data:
#     for item in line:
#         print(item['val'], end="")
#     print()


data[1][1]['cost'] = 0
data[1][1]['finished'] = True
# pprint(data)

stack = [(1, 1)]
i = 0
while len(stack) > 0:
    i += 1
    # biggest = max(stack, key=lambda x: data[x[1]][x[0]]['cost'])
    biggest = min(range(len(stack)), key=lambda x: data[stack[x][1]][stack[x][0]]['cost'])
    # print("Stack:", stack)
    # print("Biggest:", biggest)
    if i % 100 == 0:
        print(i, "/", len(data) * (len(data[0])))
    x, y = stack.pop(biggest)
    # print("X/Y:", x, y)
    data[y][x]['finished'] = True
    dirs_raw = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    dirs = [(dx, dy) for dx, dy in [(x + d[0], y + d[1]) for d in dirs_raw] if data[dy][dx] is not None]
    cost = data[y][x]['cost']
    for dx, dy in dirs:
        item = data[dy][dx]
        if item['finished']:
            continue
        if item['cost'] > cost + item['val']:
            item['cost'] = cost + item['val']
        try:
            ind = stack.index((dx, dy))
        except ValueError:
            stack.append((dx, dy))

# pprint(data)
pprint(data[len(data) - 2][len(data[0]) - 2])
