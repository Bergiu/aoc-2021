test_input = sorted(map(int, "16,1,2,0,4,2,7,1,2,14".split(",")))
input = sorted(map(int, open("input").read().split(",")))

mean = test_input[len(test_input) // 2]

mean_distance = [abs(x - mean) for x in test_input]

print("Mean Test:", mean)
print("Fuel Test:", sum(mean_distance))

mean = input[len(input) // 2]

mean_distance = [abs(x - mean) for x in input]

print("Mean:", mean)
print("Fuel:", sum(mean_distance))
