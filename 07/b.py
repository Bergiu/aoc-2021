import math

test_input = sorted(map(int, "16,1,2,0,4,2,7,1,2,14".split(",")))
input = sorted(map(int, open("input").read().split(",")))

mean = round(sum(test_input) / len(test_input))

# 11 -> 66  
# 5 -> 15   
# 4 -> 10   1 + 2 + 3 + 4
# 3 -> 6    1 + 2 + 3
# 2 -> 3    1 + 2
# 1 -> 1    1
# gauß: (n*(n+1)) / 2
mean_n = [abs(x - mean) for x in test_input]
mean_distance = [n * (n + 1) / 2 for n in mean_n]

print(mean)
print(sum(mean_distance))
print("--")

mean_unround = sum(input) / len(input)
mean_ceil = math.ceil(sum(input) / len(input))
mean_floor = math.floor(sum(input) / len(input))
mean = round(sum(input) / len(input))

mean_n = [abs(x - mean) for x in input]
mean_distance = [n * (n + 1) / 2 for n in mean_n]
mean_n_floor = [abs(x - mean_floor) for x in input]
mean_distance_floor = [n * (n + 1) / 2 for n in mean_n_floor]
mean_n_ceil = [abs(x - mean_ceil) for x in input]
mean_distance_ceil = [n * (n + 1) / 2 for n in mean_n_ceil]

print("Round mean:", mean)
print("Exact mean:", mean_unround)
print("Ceil mean:", mean_ceil)
print("Floor mean:", mean_floor)
print("Fuel round:", sum(mean_distance))
print("Fuel floor:", sum(mean_distance_floor))  # the correct one
print("Fuel ceil:", sum(mean_distance_ceil))
