# each cell has 64 bit float
# my numbers are < 6000 so they match in 2^13
# 4*13 = 52
# 52 is the size of the mantisse
# i can put 4 numbers into 1 float

shifts = 13

numbers = [int(x) for x in open("input", "r").readlines()]

# encode
new_numbers = []
last_num = 0
for i, number in enumerate(numbers):
    pos_mul = i % 4
    pos = pos_mul * shifts
    shifted = number << pos
    last_num |= shifted
    if pos_mul == 3 or i == len(numbers) - 1:
        new_numbers.append(last_num)
        last_num = 0

# decode for testing
for num in new_numbers:
    bit_block = ((2 ** shifts) - 1)
    num1 = (num >> 0 * shifts) & bit_block
    num2 = (num >> 1 * shifts) & bit_block
    num3 = (num >> 2 * shifts) & bit_block
    num4 = (num >> 3 * shifts) & bit_block
    print(num1)
    print(num2)
    print(num3)
    print(num4)


open("input_optimized", "w").writelines([f"{str(num)}\n" for num in new_numbers])
