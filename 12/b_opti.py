from __future__ import annotations
import time
from pprint import pprint
from typing import List

inp = [line.split("-") for line in open("input").read().splitlines()]


def can_continue(node: str, du_kommst_von: List[str]):
    if node.isupper():
        return True
    if du_kommst_von.count(node) < 1:
        return True
    for item in du_kommst_von:
        if item.islower() and du_kommst_von.count(item) > 1:
            return False
    if node not in ['start', 'end']:
        return True
    return False


def finde_nodes(node: str, du_kommst_von: List[str]):
    for x, y in inp:
        if x == node:
            if can_continue(y, du_kommst_von):
                yield y
        if y == node:
            if can_continue(x, du_kommst_von):
                yield x


def suche(node: str, du_kommst_von: List[str]):
    du_kommst_von.append(node)
    if node == "end":
        return 1
    new_nodes = finde_nodes(node, du_kommst_von)
    count = 0
    for new_node in new_nodes:
        count += suche(new_node, du_kommst_von)
        du_kommst_von.pop(-1)
    return count


def b():
    count = suche('start', [])
    print(count)


if __name__ == '__main__':
    b()
