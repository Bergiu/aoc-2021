from typing import List
import time
from dijkstar import Graph, find_path

file_parse_start_time = time.time()
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


data = [[int(val) for val in x]
        for x in data_expanded]
file_parse_end_time = time.time()


# for line in data:
#     for item in line:
#         print(item['val'], end="")
#     print()

graph_start_time = time.time()
graph = Graph()

len_dx = len(data[0])
len_d = len(data)
dirs_raw = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for y, line in enumerate(data):
    for x, val in enumerate(line):
        dirs = [(dx, dy) for dx, dy in [(x + d[0], y + d[1]) for d in dirs_raw]
                if 0 <= dx < len_dx and 0 <= dy < len_d]
        for dx, dy in dirs:
            graph.add_edge((dx, dy), (x, y), val)
graph_end_time = time.time()

path_find_start_time = time.time()
path = find_path(graph, (0, 0), (len(data[0]) - 1, len(data) - 1))
print(path.total_cost)
path_find_end_time = time.time()

print("Duration file parsing:   {:3.2f}s".format(file_parse_end_time - file_parse_start_time))
print("Duration graph creation: {:3.2f}s".format(graph_end_time - graph_start_time))
print("Duration path finding:   {:3.2f}s".format(path_find_end_time - path_find_start_time))
