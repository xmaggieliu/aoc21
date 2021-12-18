from collections import Counter

translation = {}

with open("input.txt", "r") as f:
    polymer = f.readline().strip()
    f.readline()
    for line in f:
        find, repl = line.strip().split(" -> ")
        translation[find] = repl

for step in range(10):
    update = ""
    for i in range(len(polymer) - 1):
        update += polymer[i]
        if polymer[i:i+2] in translation.keys():
            update += translation[polymer[i:i+2]]
    update += polymer[len(polymer) - 1]
    polymer = update

polymer = Counter(polymer).most_common()
print(polymer[0][1] - polymer[-1][1])

