basins = []
mnt = []


with open("input.txt", "r") as f:
    for line in f:
        mnt.append([int(num) for num in line.strip()])

width = len(mnt[0])
length = len(mnt)

def basin_size(coords):
    global mnt, length, width
    total = 0
    for elem in coords:
        i, j = elem[0], elem[1]
        cur = mnt[i][j]
        if i < length - 1 and cur < mnt[i + 1][j] and [i + 1, j] not in coords and mnt[i + 1][j] != 9:
            total += 1
            coords.append([i + 1, j])
        if i > 0 and cur < mnt[i - 1][j] and [i - 1, j] not in coords and mnt[i - 1][j] != 9:
            total += 1
            coords.append([i - 1, j])
        if j < width - 1 and cur < mnt[i][j + 1] and [i, j + 1] not in coords and mnt[i][j + 1] != 9:
            total += 1
            coords.append([i, j + 1])
        if j > 0 and cur < mnt[i][j - 1] and [i, j - 1] not in coords and mnt[i][j - 1] != 9:
            total += 1
            coords.append([i, j - 1])
    
    return total + 1



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
            basins.append(basin_size([[i, j]]))

maximum = max(basins)
basins.remove(maximum)
m = max(basins)
maximum *= m
basins.remove(m)
maximum *= max(basins)

print(maximum)
