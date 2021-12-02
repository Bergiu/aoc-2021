input = open("input", "r").read().split("\n")
output = []
for inp in input:
    if inp == "":
        continue
    tmp = inp.split(" ")
    op = tmp[0]
    x = tmp[1]
    table = {"forward": 1, "up": 2, "down": 3}
    op_new = table[op]
    output.append(f"{op_new} {x}\n")


open("input_converted", "w").writelines(output)
