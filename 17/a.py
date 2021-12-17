import math

inp = open("input").read().split(" ")
x_range = list(map(int, inp[2].split("=")[1].replace(",", "").split("..")))
y_range = list(map(int, inp[3].split("=")[1].replace("\n", "").split("..")))
xl, xr = x_range  # x left, x right
yd, yu = y_range  # y down, y up


def is_bigger_than_target(x, y, velo_x, velo_y):
    if velo_x > 0:
        x_bigger = x > xr
    elif velo_x < 0:
        x_bigger = x < xl
    else:
        x_bigger = not (xl <= x <= xr)
    if velo_y > 0:
        y_bigger = False
    else:
        y_bigger = y < yd
    return y_bigger or x_bigger


def is_in_range(x, y):
    return xl <= x <= xr and yd <= y <= yu


def get_path(velo_x, velo_y):
    current_x = 0
    current_y = 0
    path = []
    hit = False
    while True:
        if is_bigger_than_target(current_x, current_y, velo_x, velo_y):
            break
        if is_in_range(current_x, current_y):
            hit = True
            # break for performance optimization, not break for better visualisation
        current_x += velo_x
        current_y += velo_y
        path.append((current_x, current_y))
        if velo_x > 0:
            velo_x -= 1
        elif velo_x < 0:
            velo_x += 1
        velo_y -= 1
    if hit:
        return (path[:-1], hit)
    else:
        return (path, hit)


def plot(path):
    max_x = max([x for x, _ in path + [(0, 0), (xr, 0)]])
    max_y = max([y for _, y in path + [(0, 0), (0, yu)]])
    min_x = min([x for x, _ in path + [(0, 0), (xl, 0)]])
    min_y = min([y for _, y in path + [(0, 0), (0, yd)]])
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) == (0, 0):
                print("S", end="")
            elif (x, y) in path:
                print("#", end="")
            elif xl <= x <= xr and yd <= y <= yu:
                print("T", end="")
            else:
                print(".", end="")
        print()


def reverse_gauss(value):
    return (math.sqrt(8 * value + 1) - 1) / 2


def x_upper_limit():
    return xr


def x_lower_limit():
    return math.ceil(reverse_gauss(xl))


def y_best_limit():
    return -yd


def print_result(x, y, path, hit):
    hit_s = "Hit" if hit else "Miss"
    print("target area: x={}..{}, y={}..{} ({})".format(*x_range, *y_range, hit_s))
    print([(0, 0)] + path)
    plot(path)


def find_best():
    y = y_best_limit()
    while True:
        for x in range(x_upper_limit(), x_lower_limit() - 1, -1):
            path, hit = get_path(x, y)
            if hit:
                return x, y, path, hit
        y -= 1


def a():
    solution_x, solution_y, path, hit = find_best()
    # print_result(solution_x, solution_y, path, hit)
    y_max = max([y for _, y in path])
    print("Result:", y_max)


def main():
    a()


if __name__ == '__main__':
    main()
