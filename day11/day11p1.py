octo = []
flashes = 0


with open("input.txt", "r") as f:
    for i in range(10):
        row = list(map(int, [o for o in f.readline().strip()]))
        add = []
        for o in row:
            add.append([o, False])
        octo.append(add)


def neighbours(m, n, step):
    flashes = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
           
            if i == j == 0:
                continue
            elif m + i < 0 or n + j < 0 or m + i > 9 or n + j > 9:
                # out of range
                continue
            if octo[m+i][n+j][1]:
                continue
            octo[m + i][n + j][0] += 1
            if octo[m + i][n + j][0] > 9:
                flashes += 1
                octo[m + i][j + n][1] = True
                octo[m + i][n + j][0] = 0
                flashes += neighbours(m + i, n + j, step)
    return flashes


for step in range(1, 101):
    flash = []
    for i in range(10):
        for j in range(10):
            octo[i][j][0] += 1
            octo[i][j][1] = False
            if octo[i][j][0] > 9:
                flash.append([i, j])

    for pair in flash:
        i, j = pair[0], pair[1]
        if octo[i][j][1]:
            continue
        flashes += 1
        octo[i][j][1] = True
        octo[i][j][0] = 0
        flashes += neighbours(i, j, step)

    
print(flashes)