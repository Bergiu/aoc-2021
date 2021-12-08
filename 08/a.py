lines = open("input").read().rstrip("\n").split("\n")
outputs = [line.split(" | ")[1].split(" ") for line in lines]
countings = [len(x) for output in outputs for x in output]
print(len(list(filter(lambda x: x in [2, 4, 3, 7], countings))))
