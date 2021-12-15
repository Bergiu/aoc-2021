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


data = [[{'val': int(val), 'finished': False, 'cost': float('inf')} for val in x]
        for x in data_expanded]


# for line in data:
#     for item in line:
#         print(item['val'], end="")
#     print()


data[0][0]['cost'] = 0
data[0][0]['finished'] = True
# pprint(data)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return data[self.y][self.x]['cost'] < data[other.y][other.x]['cost']

stack: List[Node] = [Node(1, 1)]
heapq.heapify(stack)
for x in range(len(data)):
    for y in range(len(data[0])):
        heapq.heappush(stack, Node(x, y))

len_d = len(data)
len_dx = len(data[0])
dirs_raw = [(-1, 0), (1, 0), (0, 1), (0, -1)]
i = 0
while len(stack) > 0:
    i += 1
    smallest = heapq.heappop(stack)
    if i % 1000 == 0:
        print(i, "/", len(data) * (len(data[0])))
    x = smallest.x
    y = smallest.y
    # print("X/Y:", x, y)
    if data[y][x]['finished']:
        continue
    data[y][x]['finished'] = True
    dirs = [(dx, dy) for dx, dy in [(x + d[0], y + d[1]) for d in dirs_raw]
            if 0 < dx < len_dx and 0 < dy < len_d]
    cost = data[y][x]['cost']
    for dx, dy in dirs:
        item = data[dy][dx]
        if item['finished']:
            continue
        if item['cost'] > cost + item['val']:
            item['cost'] = cost + item['val']

# pprint(data)
pprint(data[len(data) - 2][len(data[0]) - 2])
