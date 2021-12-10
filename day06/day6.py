# REPLACE 256 to 80 FOR PART 1 OF DAY 6

def get_total(first):
    total = 1
    fish = [[0] * 7 for i in range(256)]
    fish[0][first] = 1
    for i in range(1, 256):
        parent = i % 7
        baby = (i + 2) % 7
        for j in range(7):
            fish[i][j] += fish[i - 1][j]
        total += fish[i][parent]
        if i + 3 < 256:
            fish[i + 3][baby] += fish[i][parent]
    return total

ending_fish = []
for i in range(5):
    ending_fish.append(get_total(i + 1))

total = 0

with open("input.txt", "r") as f:
    starting_fish = list(map(int, f.readline().strip().split(",")))

for fish in starting_fish:
    total += ending_fish[fish - 1]


print(total)

