lines = []


with open("input2.txt", "r") as f:
    for line in f:
        ls = line.split()
        lines.append([ls[0], int(ls[1])])


depth = 0
hrz_pos = 0

for command in lines:
    if command[0] == "forward":
        hrz_pos += command[1]
    elif command[0] == "up":
        depth -= command[1]
    else:
        depth += command[1]


print(depth * hrz_pos) 

