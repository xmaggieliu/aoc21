paper = []
lengthx = 1311
widthy = 895


for i in range(895):
    paper.append(["."] * 1311)


with open("input.txt", "r") as f:
    for line in f:
        if line == "\n":
            break
        else:
            x, y = map(int, line.strip().split(","))
            paper[y][x] = "#"

    dots = 0
    for line in f:
        dir, fold = line.strip("fold along \n").split("=")
        fold = int(fold)
        if dir == "x":
            for y in range(widthy):
                for x in range(fold):
                    other_side = 2 * fold - x
                    if paper[y][other_side] == "#":
                        paper[y][x] = "#"
                    if paper[y][x] == "#":
                        dots += 1
            lengthx = fold + 1
        else:
            for y in range(fold):
                for x in range(lengthx):
                    other_side = 2 * fold - y
                    if paper[other_side][x] == "#":
                        paper[y][x] = "#"
                    if paper[y][x] == "#":
                        dots += 1
            widthy = fold + 1
        # PART 1 break HERE AND PRINT dots
        
        
# PART 2 TO PRINT LETTERS
for y in range(widthy):
    for x in range(lengthx):
        print(paper[y][x], end="")
    print()
print()
