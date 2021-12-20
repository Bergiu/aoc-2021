from functools import reduce as reduce_list
import json
import math


verbose = False


def load(string):
    return json.loads(string)


def load_file(filename):
    return [load(line) for line in open(filename).read().splitlines()]


class SnailfishNumber:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self

    def __str__(self):
        return str(self.value)

    def magnitude(self):
        return self.value


class Dir:
    left = 0
    right = 1


class Pairs:
    def __init__(self, number_left, number_right):
        self.left = number_left
        self.right = number_right

    def magnitude(self):
        return self.left.magnitude() * 3 + self.right.magnitude() * 2

    def __iter__(self):
        yield from self.left
        yield self
        yield from self.right

    def explode(self):
        explode_node = self.search_explode(1)
        if explode_node:
            left = self.find_left(explode_node)
            right = self.find_right(explode_node)
            upper, dir = self.find_upper(explode_node)
            if dir == Dir.left:
                if left is not None:
                    left.value += explode_node.left.value
                if right is not None:
                    right.value += explode_node.right.value
                upper.left = SnailfishNumber(0)
            else:
                if left is not None:
                    left.value += explode_node.left.value
                if right is not None:
                    right.value += explode_node.right.value
                upper.right = SnailfishNumber(0)
            return True
        return False

    def split(self):
        if isinstance(self.left, SnailfishNumber):
            vl = self.left.value
            if vl >= 10:
                self.left = Pairs(
                    SnailfishNumber(vl // 2),
                    SnailfishNumber(math.ceil(vl / 2))
                )
                return True
        else:
            if self.left.split():
                return True
        if isinstance(self.right, SnailfishNumber):
            vl = self.right.value
            if vl >= 10:
                self.right = Pairs(
                    SnailfishNumber(vl // 2),
                    SnailfishNumber(math.ceil(vl / 2))
                )
                return True
        else:
            if self.right.split():
                return True
        return False

    def find_upper(self, node):
        if self.left == node:
            return self, Dir.left
        if self.right == node:
            return self, Dir.right
        else:
            if isinstance(self.left, Pairs):
                lnode = self.left.find_upper(node)
                if lnode is not None:
                    return lnode
            if isinstance(self.right, Pairs):
                rnode = self.right.find_upper(node)
                return rnode

    def find_left(self, node):
        second_last_fish = None
        last_fish = None
        for x in self:
            if isinstance(x, SnailfishNumber):
                second_last_fish = last_fish
                last_fish = x
            if x == node:
                return second_last_fish

    def find_right(self, node):
        self_node = None
        next_fish = None
        for x in self:
            if x == node:
                self_node = x
            if self_node is not None:
                if isinstance(x, SnailfishNumber):
                    if next_fish is None:
                        next_fish = True
                    else:
                        return x

    def search_explode(self, deepth):
        if deepth >= 5:
            return self
        if isinstance(self.left, Pairs):
            lnode = self.left.search_explode(deepth + 1)
            if lnode is not None:
                return lnode
        if isinstance(self.right, Pairs):
            rnode = self.right.search_explode(deepth + 1)
            return rnode

    def to_str(self, deepth):
        out = f"[({deepth}) "
        if isinstance(self.left, Pairs):
            out += self.left.to_str(deepth + 1)
        else:
            out += str(self.left.value)
        out += ", "
        if isinstance(self.right, Pairs):
            out += self.right.to_str(deepth + 1)
        else:
            out += str(self.right.value)
        out += "]"
        return out

    def __str__(self):
        return f"[{self.left},{self.right}]"


def convert(l):
    if isinstance(l, list):
        new_l = [convert(x) for x in l]
        return Pairs(new_l[0], new_l[1])
    else:
        return SnailfishNumber(l)


def add_pairs(pair1, pair2):
    return Pairs(pair1, pair2)


def test_explode():
    tests = [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
    ]
    for t, res in tests:
        conv = convert(load(t))
        conv.explode()
        assert str(conv) == res


def reduce(pair1, pair2):
    conv = add_pairs(pair1, pair2)
    if verbose:
        print("After addition:", conv)
    old = str(conv)
    while True:
        exploded = conv.explode()
        if exploded:
            if verbose:
                print("After explode: ", conv)
            continue
        splitted = conv.split()
        if splitted:
            if verbose:
                print("After split:   ", conv)
            continue
        break
    return conv


def test_add_pairs():
    tests = [
        (["[1,2]", "[[3,4],5]"], "[[1,2],[[3,4],5]]"),
    ]
    for t, res in tests:
        converted_numbers = [convert(load(x)) for x in t]
        a = add_pairs(*converted_numbers)
        assert str(a) == res


def test():
    tests = [
        (["[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"], "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
        (["[1,1]", "[2,2]", "[3,3]", "[4,4]"], "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
        (["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]"], "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
        (["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"], "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
        (["[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]", "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]", "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]", "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]", "[7,[5,[[3,8],[1,4]]]]", "[[2,[2,2]],[8,[8,1]]]", "[2,9]", "[1,[[[9,3],9],[[9,0],[0,7]]]]", "[[[5,[7,4]],7],1]", "[[[[4,2],2],6],[8,7]]"], "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
    ]
    for t, res in tests:
        converted_numbers = [convert(load(x)) for x in t]
        if verbose:
            print(" + ".join([str(x) for x in converted_numbers]))
        a = reduce_list(reduce, converted_numbers)
        assert str(a) == res


def a_test():
    inp = load_file("input_test")
    converted_numbers = [convert(x) for x in inp]
    res = reduce_list(reduce, converted_numbers)
    assert str(res) == "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
    assert res.magnitude() == 4140


def a():
    inp = load_file("input")
    converted_numbers = [convert(x) for x in inp]
    res = reduce_list(reduce, converted_numbers)
    print(res.magnitude())

if __name__ == '__main__':
    test_add_pairs()
    test_explode()
    test()
    a_test()
    a()
