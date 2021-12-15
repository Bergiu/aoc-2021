# GENERATED MEMORY:
# [0]: Length of cells for dot list (n)
# [1]: Bits per number in one float
# [2]: Real length of dot list
# [3;n+3): dot list decoded
#          6,10,0,14,9,10...
#          x1,y1,x2,y2...
# [n+3]: Length of cells for fold list (m)
# [n+4]: Bits per number in one float
# [n+5]: Real length of fold list
# [n+6;m+n+6): Fold instruction array decoded
#              0,7,1,5
#              DIR1,VAL1,DIR2,VAL2
#              DIR = 1 represents 'x'
#              DIR = 0 represents 'y'


import math
from typing import List
from dataclasses import dataclass

inp_dots, inp_folds = open("input").read().split("\n\n")


dots = [int(y) for x in inp_dots.split("\n") for y in x.split(',')]
folds_s = [x.split(" ")[2].split("=") for x in inp_folds.rstrip().split("\n")]
folds = []
for fold_s in folds_s:
    dir = 1 if fold_s[0] == 'x' else 0
    folds.append(dir)
    folds.append(int(fold_s[1]))


FLOAT_USABLE_BIT_LENGTH = 52

print("Dots Len:", len(dots))
print("Dots Max:", max(dots))
print("Dots Min:", min(dots))
print("Folds Len:", len(folds))
print("Folds Max:", max(folds))
print("Folds Min:", min(folds))

# Range: 0-99 < 128 = 2^7, 7 bit
# 52 bit / 7 bit = 7 numbers per float
# Len: 100, 100/7 = 14 cells


@dataclass
class EncodeOptions:
    numbers_per_float: int = 0
    amount_of_floats: int = 0
    bit_per_number: int = 0


def get_encode_options(l):
    if min(l) < 0:
        raise Exception("Numbers < 0")
    max_number = max(l)
    # amount of bits that is needed for one number
    bit_per_number = FLOAT_USABLE_BIT_LENGTH  # maximum
    for pot in range(FLOAT_USABLE_BIT_LENGTH):
        if 2 ** pot > max_number:
            bit_per_number = pot
            break
    # amount of numbers that are encoded into one float (one float = one cell)
    numbers_per_float = FLOAT_USABLE_BIT_LENGTH // bit_per_number
    # amount of floats that is needed to save all numbers
    amount_of_floats = math.ceil(len(l) / numbers_per_float)
    if amount_of_floats > 510:
        raise Exception("To much cells")
    return EncodeOptions(numbers_per_float, amount_of_floats, bit_per_number)


def encode(l):
    encode_options = get_encode_options(l)
    new_numbers: List[int] = []
    last_num = 0
    for i, number in enumerate(l):
        pos_mul = i % encode_options.numbers_per_float
        pos = pos_mul * encode_options.bit_per_number
        shifted = number << pos
        last_num |= shifted
        if pos_mul == encode_options.numbers_per_float - 1 or i == len(l) - 1:
            new_numbers.append(last_num)
            last_num = 0
    out = new_numbers
    out.insert(0, len(new_numbers))
    out.insert(1, encode_options.bit_per_number)
    out.insert(2, len(l))
    return out


def decode(l_original, l_encoded):
    # decode for testing
    length = l_encoded[0]
    bit_per_number = l_encoded[1]
    length_real = l_encoded[2]
    old_numbers = []
    len_real_i = 0
    for num in l_encoded[3:]:
        bit_block = ((2 ** bit_per_number) - 1)
        for i in range(FLOAT_USABLE_BIT_LENGTH // bit_per_number):
            if len_real_i >= length_real:
                break
            num_decoded = (num >> i * bit_per_number) & bit_block
            old_numbers.append(num_decoded)
            len_real_i += 1
    assert l_original == old_numbers
    assert length_real == len(old_numbers)


dots_encoded = encode(dots)
decode(dots, dots_encoded)

print("Len Dots Encoded:", len(dots_encoded))

folds_encoded = encode(folds)
decode(folds, folds_encoded)
print("Len Folds Encoded:", len(folds_encoded))

out = []
out.extend(dots_encoded)
out.extend(folds_encoded)

print("Len All Encoded:", len(out))

open("input_optimized", "w").writelines([f"{str(num)}\n" for num in out])
