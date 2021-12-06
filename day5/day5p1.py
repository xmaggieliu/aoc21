vents = []
for i in range(1000):
    vent = []
    for j in range(1000):
        vent.append(0)
    vents.append(vent)

with open("input5.txt", "r") as f:
    for line in f:
        line = line.split()
        x1, y1 = list(map(int, line[0].split(",")))
        x2, y2 = list(map(int, line[2].split(",")))

        if x2 == x1:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                vents[x2][i] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                vents[i][y1] += 1
        else:   
            n = (y2 - y1)/(x2 - x1)
            if n > 0:
                y = min(y1, y2)
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    vents[i][y] += 1
                    y += 1
            else:
                y = min(y1, y2)
                for i in range(max(x1, x2), min(x1, x2) - 1, -1):
                    vents[i][y] += 1
                    y += 1


total = 0

for vent in vents:
    for v in vent:
        if v >= 2:
            total += 1

print(total)


# low: 12334