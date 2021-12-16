from typing import List, Tuple
from functools import reduce
import ply.lex as lex
import ply.yacc as yacc

parser_i = 0
inp = ""


def next(n=1):
    global parser_i, inp
    out = inp[parser_i: parser_i + n]
    parser_i += n
    return out


def nexti(n=1):
    return int(next(n), 2)


def next_literal_value():
    out = []
    last_lv = 1
    while last_lv == 1:
        last_lv = nexti(1)
        lv = next(4)
        out.append(lv)
    return int("".join(out), 2)


def next_package():
    version = nexti(3)
    type_id = nexti(3)
    sub_packages = []
    if type_id == 4:
        # read lvs
        return next_literal_value()
    # read subpackages
    length_type_id = nexti(1)
    if length_type_id == 0:
        # 15bits
        total_length_in_bits = nexti(15)
        parser_i_max = parser_i + total_length_in_bits
        while parser_i < parser_i_max:
            package = next_package()
            sub_packages.append(package)
    else:
        # 11bits
        number_of_subpackets_contained = nexti(11)
        for _ in range(number_of_subpackets_contained):
            package = next_package()
            sub_packages.append(package)
    # execute operation
    if type_id == 0:
        return sum(sub_packages)
    if type_id == 1:
        return reduce(lambda x, y: x * y, sub_packages)
    if type_id == 2:
        return min(sub_packages)
    if type_id == 3:
        return max(sub_packages)
    if type_id == 5:
        return 1 if sub_packages[0] > sub_packages[1] else 0
    if type_id == 6:
        return 1 if sub_packages[0] < sub_packages[1] else 0
    if type_id == 7:
        return 1 if sub_packages[0] == sub_packages[1] else 0
    raise Exception("Invalid operation.")


def start(filename):
    global inp, parser_i
    inp = "".join(["{:04b}".format(int(x, 16)) for x in open(filename).read().strip()])
    parser_i = 0
    return next_package()


def start_manual(string):
    global inp, parser_i
    inp = "".join(["{:04b}".format(int(x, 16)) for x in string])
    parser_i = 0
    return next_package()


def test():
    tests = [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ]
    for case, result in tests:
        package = start_manual(case)
        # print("Test", case, package, "==", result)
        assert package == result


def main():
    test()
    package = start("input")
    print(package)


if __name__ == '__main__':
    main()
