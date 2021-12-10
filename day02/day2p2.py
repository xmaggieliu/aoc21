lines = []


with open("input2.txt", "r") as f:
    for line in f:
        ls = line.split()
        lines.append([ls[0], int(ls[1])])


depth, hrz_pos, aim = 0, 0, 0

for command in lines:
    if command[0] == "forward":
        hrz_pos += command[1]
        depth += aim * command[1]
    elif command[0] == "up":
        aim -= command[1]
    else:
        aim += command[1]


print(depth * hrz_pos) 

