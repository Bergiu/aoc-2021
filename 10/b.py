from parser import *


FILENAME = "input"
LINT = True


if __name__ == '__main__':
    data = open(FILENAME).read()
    setup(LINT, FILENAME)
    do_parsing(data)
    point_map = {'LROUND': 1, 'LSQUARE': 2, 'LCURLY': 3, 'LANGLE': 4}
    corrupted_first = [x for x, _, _ in corrupted]
    only_incompletes = [x for x in incomplete if x[0] not in corrupted_first]
    points = []
    for only_incomplete in only_incompletes:
        line_points = 0
        # print("".join([x.value for x in reversed(only_incomplete[3]) if isinstance(x, lex.LexToken)]))
        for x in reversed(only_incomplete[3]):
            if isinstance(x, lex.LexToken):
                line_points *= 5
                line_points += point_map[x.type]
        points.append(line_points)
    print(sorted(points)[len(points) // 2])
