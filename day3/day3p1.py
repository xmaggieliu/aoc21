lines = [0] * 12
count = 0
gamma = ""
epsilon = ""


with open("input3.txt", "r") as f:
    for line in f:
        bits = [char for char in line.strip("\n")]
        lines = [lines[i] + 1 if bits[i] == "1" else lines[i] for i in range(12)]
        count += 1


for elem in lines:
    if elem > count - elem:
        gamma += "1"
        epsilon += "0"
    else: 
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)
