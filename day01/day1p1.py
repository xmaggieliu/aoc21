lines = []

with open("input1.txt", "r") as f:
    for line in f:
        lines.append(int(line.strip("\n")))


lines = list(map(int, lines))

count = 0

for i in range(len(lines) - 1):
    if lines[i + 1] - lines[i] > 0:
        count += 1

print(count)
