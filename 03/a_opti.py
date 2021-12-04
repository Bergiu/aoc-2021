# second try
filename = "input"
input = open(filename).read().split()
line_len = len(input[0])  # size of one word (one word every line)
data = [int(x, 2) for x in input]
# count_size = math.ceil(math.log(len(input), 2))
count_size = 10  # size for every counter in the counting variable
# amount_bits_that_match_in_one_counter = 52 // count_size = 5
# amount_counters = math.ceil(line_len / amount_bits_that_match_in_one_counter) = 3
count1 = 0  # needed for line_len < 5 (5*10 = 50 < 52)
count2 = 0  # needed for line_len < 10
count3 = 0  # needed for line_len < 15

for number in data:
    for bit_pos in range(0, min(5, line_len)):
        # 0
        moved_number = number >> bit_pos  # move current pos to right
        bit = moved_number & 1  # and mask every other bit
        count1 += bit << (count_size * bit_pos)
    for bit_pos in range(5, min(10, line_len)):
        moved_number = number >> bit_pos  # move current pos to right
        bit = moved_number & 1  # and mask every other bit
        count2 += bit << (count_size * (bit_pos - 5))
    for bit_pos in range(10, min(15, line_len)):
        moved_number = number >> bit_pos  # move current pos to right
        bit = moved_number & 1  # and mask every other bit
        count3 += bit << (count_size * (bit_pos - 10))


half = len(data) / 2

mask = (1 << count_size) - 1  # 00001111
gamma = 0
for word_pos in range(0, min(5, line_len)):
    count = (count1 >> (count_size * word_pos)) & mask
    gamma |= (1 << word_pos) * int(count >= half)
for word_pos in range(5, min(10, line_len)):
    count = (count2 >> (count_size * (word_pos - 5))) & mask
    gamma |= (1 << word_pos) * int(count >= half)
for word_pos in range(10, min(15, line_len)):
    count = (count3 >> (count_size * (word_pos - 10))) & mask
    gamma |= (1 << word_pos) * int(count >= half)


invert = gamma ^ ((1 << line_len) - 1)
print("count1", count1)
print("count2", count2)
print("count3", count3)
print("gamma: ", gamma, format(gamma, 'b').zfill(12))
print("invert: ", invert, format(invert, 'b').zfill(12))
print(gamma * invert)
