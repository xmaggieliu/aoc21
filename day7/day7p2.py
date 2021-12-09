with open("input.txt", "r") as f:
    crabs = list(map(int, f.readline().strip().split(",")))

align = int(sum(crabs) / len(crabs))

fuel = 0

for position in crabs:
    n = abs(position - align)
    fuel += int((n * (n + 1)) / 2)

print(fuel)
