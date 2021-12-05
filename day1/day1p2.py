lines = []

with open("input1.txt", "r") as f:
    for line in f:
        lines.append(int(line.strip("\n")))

count = 0

for i in range(len(lines) - 3):
    if lines[i + 3] - lines[i] > 0:
        count += 1

print(count)
