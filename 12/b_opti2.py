from __future__ import annotations
import time
from pprint import pprint
from typing import List, Dict, Tuple

inp = [line.split("-") for line in open("input").read().splitlines()]


counts = {}
for x, y in inp:
    if x not in counts.keys():
        counts[x] = [0, x.islower()]
    if y not in counts.keys():
        counts[y] = [0, y.islower()]


def can_continue(node: str, du_kommst_von: Dict[str, List[int, bool]]):
    if node.isupper():
        return True
    if du_kommst_von[node][0] < 1:
        return True
    for count, lower in du_kommst_von.values():
        if lower and count > 1:
            return False
    if node not in ['start', 'end']:
        return True
    return False


def finde_nodes(node: str, du_kommst_von: Dict[str, List[int, bool]]):
    for x, y in inp:
        if x == node:
            if can_continue(y, du_kommst_von):
                yield y
        if y == node:
            if can_continue(x, du_kommst_von):
                yield x


def suche(node: str, du_kommst_von: Dict[str, List[int, bool]]):
    if node == "end":
        return 1
    du_kommst_von[node][0] += 1
    new_nodes = finde_nodes(node, du_kommst_von)
    count = 0
    for new_node in new_nodes:
        count += suche(new_node, du_kommst_von)
    du_kommst_von[node][0] -= 1
    return count


def b():
    count = suche('start', counts)
    print(count)


if __name__ == '__main__':
    b()
