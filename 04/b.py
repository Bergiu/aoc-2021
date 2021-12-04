input = open("input").read().split("\n\n")
grids_tmp = input[1::]
grids_tmp = [block.strip().split("\n") for block in grids_tmp]
grids = []
for block in grids_tmp:
    tmp = []
    for line in block:
        tmp.append(list(map(int, filter(None, line.strip().split(" ")))))
    grids.append(tmp)
choosens = list(map(int, input[0].split(",")))

def a():
    for choosen in choosens:
        i = 0
        while i < len(grids):
            block = grids[i]
            for line in block:
                for pos, char in enumerate(line):
                    if char == choosen:
                        line[pos] = None
            for x in range(5):
                l_x = 0
                l_y = 0
                for y in range(5):
                    if block[x][y] is None:
                        l_x += 1
                    if block[y][x] is None:
                        l_y += 1
                if l_x == 5 or l_y == 5:
                    if len(grids) == 1:
                        result = choosen * sum(map(sum, filter(None, [filter(None, line) for line in block])))
                        return result
                    else:
                        grids.pop(i)
                        i -= 1
                        break
            i += 1


if __name__ == '__main__':
    result = a()
    print(result)
