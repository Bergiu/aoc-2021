lines = open("input").read().split("\n")
outputs = [line.split("|")[1][1:].split(" ") for line in lines if line != ""]
countings = [len(x) for output in outputs for x in output]
print(len(list(filter(lambda x: x == 2 or x == 4 or x == 3 or x == 7, countings))))
