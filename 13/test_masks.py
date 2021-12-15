def mask(full_length, bit_length, pos, old_number, new_number):
    mask_left = (2 ** (full_length - (bit_length * (pos + 1)))) - 1 << (bit_length * (pos + 1))
    if pos > 0:
        mask_right = (2 ** (bit_length * (pos))) - 1
    else:
        mask_right = 0
    mask_old = mask_left | mask_right
    mask_new = (2 ** bit_length) - 1
    old_number_enc = mask_old & old_number
    new_number_enc = (mask_new & new_number) << (bit_length * pos)
    new_entry = old_number_enc | new_number_enc
    print("-" * 10)
    print("BlockSize: " + str(bit_length))
    print(("Old : {:0" + str(full_length) + "b}").format(old_number))
    print(("NewE: {:0" + str(full_length) + "b}").format(new_number_enc))
    print(("Mask: {:0" + str(full_length) + "b}").format(mask_old))
    print(("New : {:0" + str(full_length) + "b}").format(new_entry))


for x in range(15 // 3):
    mask(15, 3, x, 2680, 2)
