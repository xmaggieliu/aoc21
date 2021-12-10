risk_lvl = 0
mnt = []


with open("input.txt", "r") as f:
    for line in f:
        mnt.append([int(num) for num in line.strip()])

width = len(mnt[0])
length = len(mnt)

for i in range(length):
    for j in range(width):
        lowest = True
        cur = mnt[i][j]
        if i < length - 1 and cur >= mnt[i + 1][j]:
            lowest = False
        elif i > 0 and cur >= mnt[i - 1][j]:
            lowest = False
        elif j < width - 1 and cur >= mnt[i][j + 1]:
            lowest = False
        elif j > 0 and cur >= mnt[i][j - 1]:
            lowest = False
        else:
            lowest = True
        if lowest:
            risk_lvl += cur + 1

print(risk_lvl)

