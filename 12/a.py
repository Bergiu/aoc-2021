from __future__ import annotations
from pprint import pprint
from typing import List

inp = [line.split("-") for line in open("input").read().splitlines()]

graph = {}


for x, y in inp:
    if x in graph.keys():
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph.keys():
        graph[y].append(x)
    else:
        graph[y] = [x]


counter = {}
for x, y in inp:
    counter[x] = 0
    counter[y] = 0


def can_continue(node: str, du_kommst_von: List[str]):
    if node.isupper():
        return True
    if du_kommst_von.count(node) >= 1:
        return False
    return True


def finde_nodes(node: str, du_kommst_von: List[str]):
    for x, y in inp:
        if x == node:
            if can_continue(y, du_kommst_von):
                yield y
        if y == node:
            if can_continue(x, du_kommst_von):
                yield x

gefunden = []
def suche(node: str, du_kommst_von: List[str]):
    du_kommst_von.append(node)
    if node == "end":
        gefunden.append([x for x in du_kommst_von])
    new_nodes = finde_nodes(node, du_kommst_von)
    for new_node in new_nodes:
        gefunden.append(suche(new_node, du_kommst_von))
        du_kommst_von.pop(-1)


if __name__ == '__main__':
    suche('start', [])
    print(len(list(filter(None, gefunden))))
