with open("input.txt", "r") as f:
    crabs = sorted(list(map(int, f.readline().strip().split(","))))

align = crabs[int(len(crabs) / 2)]

fuel = 0

for position in crabs:
    fuel += abs(position - align)

print(fuel)
