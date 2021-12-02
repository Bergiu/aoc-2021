from typing import List


shifts = 13

raw_numbers = [x for x in open("input_test_converted", "r").readlines()]
numbers: List[int] = []
for number in raw_numbers:
    if number == "":
        continue
    tmp = number.split(" ")
    numbers.append(int(tmp[0]))
    numbers.append(int(tmp[1]))


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


open("input_test_optimized", "w").writelines([f"{str(num)}\n" for num in new_numbers])
