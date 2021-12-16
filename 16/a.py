import ply.lex as lex
import ply.yacc as yacc
from typing import List, Tuple

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
    return out


version_t = int
type_id_t = int
lvs_type = List[str]
sub_packages = List['package_t']
package_t = Tuple[version_t, type_id_t, lvs_type, sub_packages]


def next_package():
    version = nexti(3)
    type_id = nexti(3)
    lvs = []
    sub_packages = []
    if type_id == 4:
        lvs = next_literal_value()
    else:
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
            for x in range(number_of_subpackets_contained):
                package = next_package()
                sub_packages.append(package)
    package = (version, type_id, lvs, sub_packages)
    return package


def start(filename):
    global inp, parser_i
    inp = "".join(["{:04b}".format(int(x, 16)) for x in open(filename).read().strip()])
    parser_i = 0
    return next_package()


def count_versions(package):
    stack = package[3]
    count = package[0]
    while len(stack) > 0:
        item = stack.pop(0)
        count += item[0]
        stack.extend(item[3])
    return count


def test():
    package = start("input_test1")
    assert count_versions(package) == 16
    print("Test 1 success.")
    package = start("input_test2")
    assert count_versions(package) == 12
    print("Test 2 success.")
    package = start("input_test3")
    assert count_versions(package) == 23
    print("Test 3 success.")
    package = start("input_test4")
    assert count_versions(package) == 31
    print("Test 4 success.")


test()
package = start("input")
print(count_versions(package))
