# first try
filename = "input"
input = open(filename).read().split()
line_len = len(input[0])  # size of one word (one word every line)
data = [int(x, 2) for x in input]
count_size = 10  # size for every counter in the counting variable
count1 = 0  # needed for line_len < 5 (5*10 = 50 < 52)
count2 = 0  # needed for line_len < 10
count3 = 0  # needed for line_len < 15

counter_liste = [0] * 12
for number in data:
    bit_pos = 0
    while bit_pos < 12:
        # 0
        moved_number = number >> bit_pos  # move current pos to right
        bit = moved_number & 1  # and mask every other bit
        counter_liste[bit_pos] += bit
        # count1 += bit << count_size * bit_pos
        bit_pos += 1


half = len(data) / 2
gamma_s = ""
for counter in counter_liste[::-1]:
    gamma_s += str(int(counter > half))


gamma = int(gamma_s, 2)


invert = gamma ^ ((1 << line_len) - 1)
print("gamma: {}, {}", gamma, format(gamma, 'b').zfill(12))
print("invert: {}, {}", invert, format(invert, 'b').zfill(12))
print(gamma * invert)
