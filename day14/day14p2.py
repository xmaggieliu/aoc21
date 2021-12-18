import copy

translation = {}

with open("input.txt", "r") as f:
    template = f.readline().strip()
    f.readline()
    for line in f:
        find, repl = line.strip().split(" -> ")
        translation[find] = repl

polymer = {elem : 0 for elem in translation.keys()}

for i in range(len(template) - 1):
    polymer[template[i:i+2]] += 1

for step in range(40):
    new_poly = copy.deepcopy(polymer)
    for key, value in translation.items():
        new_poly[key] -= polymer[key]
        new_poly[key[0] + value] += polymer[key]
        new_poly[value + key[1]] += polymer[key]
    polymer = new_poly

count = {}

for key, value in polymer.items():
    if key[0] not in count.keys():
        count[key[0]] = 0

    if key[1] not in count.keys():
        count[key[1]] = 0
    count[key[0]] += value
    count[key[1]] += value

print(int((max(count.values()) - min(count.values())) / 2))
