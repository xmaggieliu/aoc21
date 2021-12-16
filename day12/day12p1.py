caves = {}

with open("input.txt", "r") as f:
    for line in f:
        begin, end = line.strip().split("-")
        if begin in caves.keys():
            caves[begin].append(end)
        else:
            caves[begin] = [end]
        if end in caves.keys():
            caves[end].append(begin)
        else:
            caves[end] = [begin]

def route(cave, used, count):
    paths = 0
    for adj in caves[cave]:
        if adj == "end":
            paths += 1
            continue
        if adj not in used:
            new_used = []
            if adj.islower():
                new_used.append(adj)
            if adj in caves.keys():
                paths += route(adj, used[:] + new_used, count + 1)

    return paths


paths = route("start", ["start"], 0)

print(paths)
