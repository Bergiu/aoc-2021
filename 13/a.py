inp_dots, inp_folds = open("input").read().split("\n\n")

dots = [list(map(int, x.split(','))) for x in inp_dots.split("\n")]
folds = [x.split(" ")[2].split("=") for x in inp_folds.rstrip().split("\n")]
max_x = 0
max_y = 0
for x, y in dots:
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y


def print_dots():
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if [x, y] in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()


def a():
    global dots, max_x, max_y
    for dir, val_s in folds[:1]:
        val = int(val_s)
        # print("Fold", dir, val)
        if dir == 'x':
            to_fold = list(filter(lambda c: c[0] > val, dots))
            to_drop = filter(lambda c: c[0] == val, dots)
            for c in to_fold:
                new_p = [val - (c[0] - val), c[1]]
                if new_p not in dots:
                    dots.append(new_p)
            max_x = (max_x - 1) // 2
            for fold in to_fold:
                dots.remove(fold)
        else:
            to_fold = list(filter(lambda c: c[1] > val, dots))
            to_drop = filter(lambda c: c[1] == val, dots)
            for c in to_fold:
                new_p = [c[0], val - (c[1] - val)]
                if new_p not in dots:
                    dots.append(new_p)
            max_y = (max_y - 1) // 2
            for fold in to_fold:
                dots.remove(fold)
        # print("---")
        # print_dots()


# print_dots()
a()
print(len(dots))
# print_dots()
