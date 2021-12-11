filename = "input"
rounds = 100

inp = [list(map(int, x)) for x in open(filename).read().splitlines()]
data = []
for i, line in enumerate(inp):
    for j, x in enumerate(line):
        data.append([i, j, x])


def print_data():
    for i in range(10):
        for j in range(10):
            print(data[i * 10 + j][2], end="")
        print()
    print()

print_data()
flash = 0
for round in range(rounds):
    # increase
    for item in data:
        item[2] += 1
    # flash
    find_9 = list(filter(lambda part: part[2] > 9, data))
    for item in find_9:
        directions = [
            (item[0] - 1, item[1]),
            (item[0] - 1, item[1] - 1),
            (item[0] - 1, item[1] + 1),
            (item[0] + 1, item[1]),
            (item[0] + 1, item[1] - 1),
            (item[0] + 1, item[1] + 1),
            (item[0], item[1] - 1),
            (item[0], item[1] + 1)
        ]
        adjacents = [data[dir[0] * 10 + dir[1]] for dir in directions
                    if 0 <= dir[0] < 10 and 0 <= dir[1] < 10]
        for adjacent in adjacents:
            if adjacent[2] == 9:
                adjacent[2] = 0
                find_9.append(adjacent)
            elif adjacent[2] != 0:
                adjacent[2] += 1
        item[2] = 0
        flash += 1
    print_data()

print("Flashes: ", flash)
