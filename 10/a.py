from parser import *


FILENAME = "input"
LINT = True


if __name__ == '__main__':
    data = open(FILENAME).read()
    setup(LINT, FILENAME)
    do_parsing(data)
    point_map = {'RROUND': 3, 'RSQUARE': 57, 'RCURLY': 1197, 'RANGLE': 25137}
    # reverse order to overwrite with the first item at last
    # filters the first element of every line
    corrupted_first = {x: z for x, _, z in corrupted[::-1]}  # XXX
    print(sum(map(point_map.get, corrupted_first.values())))
