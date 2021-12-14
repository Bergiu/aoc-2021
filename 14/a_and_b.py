import time

start = time.time()
repeats = 40
polymer_template, pair_insertions_tmp = open("input").read().split("\n\n")
pair_insertions = [x.split(" -> ") for x in pair_insertions_tmp.splitlines()]

polymer_buckets = {}

for i in range(len(polymer_template) - 1):
    pair = polymer_template[i:i + 2]
    if pair not in polymer_buckets.keys():
        polymer_buckets[pair] = 1
    else:
        polymer_buckets[pair] += 1


for pair, target in pair_insertions:
    if pair not in polymer_buckets.keys():
        polymer_buckets[pair] = 0


for x in range(repeats):
    operations = []
    for pair, target in pair_insertions:
        if pair not in polymer_buckets.keys():
            continue
        current_pair_count = polymer_buckets[pair]
        # jetzt sind z.b. 5 mal NC da, das heißt ich muss 5 mal NB und BC erhöhen
        # und NC um 5 verringern setzen
        operations.append((pair, -current_pair_count))
        new_pairs = [pair[0] + target, target + pair[1]]
        for new_pair in new_pairs:
            operations.append((new_pair, current_pair_count))
    for pair, operation in operations:
        if pair not in polymer_buckets.keys():
            polymer_buckets[pair] = operation
        else:
            polymer_buckets[pair] += operation


# print(list(filter(lambda x: x[1] > 0, polymer_buckets.items())))

chars_count = {}
for key, value in polymer_buckets.items():
    if value <= 0:
        continue
    for character in key:
        if character not in chars_count.keys():
            chars_count[character] = 0.5 * value
        else:
            chars_count[character] += 0.5 * value

start_end = [polymer_template[:1], polymer_template[-1:]]
for x in start_end:
    chars_count[x] += 0.5


# print(chars_count)
print(max(chars_count.values()) - min(chars_count.values()))
end = time.time()
print("Duration: {:6.3f}ms".format((end - start) * 1000))
