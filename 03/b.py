filename = "input"
input = open(filename).read().split()
line_len = len(input[0])  # size of one word (one word every line)
data = [int(x, 2) for x in input]

counter_liste = [0] * 12
for number in data:
    for bit_pos in range(0, 12):
        moved_number = number >> bit_pos  # move current pos to right
        bit = moved_number & 1  # and mask every other bit
        counter_liste[bit_pos] += bit

half = len(data) / 2

print(counter_liste)


def oxygen_filter(number, bit_pos):
    moved_number = number >> bit_pos
    bit = moved_number & 1
    mcv = int(counter_liste[bit_pos] >= half)
    return mcv == bit


def co2_filter(number, bit_pos):
    moved_number = number >> bit_pos
    bit = moved_number & 1
    mcv = int(counter_liste[bit_pos] <= half)
    return mcv == bit


number_stack = [x for x in data]
for bit_pos in range(0, 12)[::-1]:
    if len(number_stack) > 1:
        number_stack_new = []
        for inp in number_stack:
            if oxygen_filter(inp, bit_pos):
                number_stack_new.append(inp)
        number_stack = number_stack_new

x1 = number_stack[0]

number_stack = [x for x in data]
for bit_pos in range(0, 12)[::-1]:
    print(bit_pos)
    print(number_stack)
    if len(number_stack) > 1:
        number_stack_new = []
        for inp in number_stack:
            if co2_filter(inp, bit_pos):
                number_stack_new.append(inp)
        number_stack = number_stack_new

x2 = number_stack[0]

print([int(c >= half) for c in counter_liste])
print(x1)
print(x2)
