from parse import parse
import numpy as np


def main():
    lines = [parse("{:d},{:d} -> {:d},{:d}\n", line) for line in open("input")]
    points = [((line[0], line[1]), (line[2], line[3])) for line in lines]
    matrix = make_matrix(points)
    print(len(list(filter(lambda x: x > 1, matrix.values()))))


def make_matrix(points):
    matrix = {}
    for p, q in points:
        x1, y1 = p
        x2, y2 = q
        sub = np.subtract(p, q)
        if sub[0] == 0:
            # vertikal
            d_x = 0
            d_y = sub[1] / abs(sub[1])
        elif sub[1] == 0:
            # horizontal
            d_x = sub[0] / abs(sub[0])
            d_y = 0
        else:
            # diagonal (x = y)
            d_x = sub[0] / abs(sub[0])
            d_y = sub[1] / abs(sub[0])
        while x1 != x2 or y1 != y2:
            coord = (x1, y1)
            if coord in matrix.keys():
                matrix[coord] += 1
            else:
                matrix[coord] = 1
            x1 -= d_x
            y1 -= d_y
        coord = (x1, y1)
        if coord in matrix.keys():
            matrix[coord] += 1
        else:
            matrix[coord] = 1
    return matrix


if __name__ == '__main__':
    main()
