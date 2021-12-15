from dataclasses import dataclass, field
from typing import Any
from pprint import pprint
from operator import itemgetter
import heapq

data = [
    [None, *[
        {'val': int(val), 'finished': False, 'cost': float('inf'), 'route': []}
        for val in x
    ], None]
    for x in open("input_test").read().splitlines()]
data.insert(0, [None] * len(data[0]))
data.append([None] * len(data[0]))

data[1][1]['cost'] = 0
data[1][1]['finished'] = True
# pprint(data)

stack = [(1, 1)]
while len(stack) > 0:
    # biggest = max(stack, key=lambda x: data[x[1]][x[0]]['cost'])
    biggest = min(range(len(stack)), key=lambda x: data[stack[x][1]][stack[x][0]]['cost'])
    # print("Stack:", stack)
    # print("Biggest:", biggest)
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

pprint(data[len(data) - 2][len(data[0]) - 2])
