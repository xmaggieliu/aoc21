li = [0] * 12
lj = [0] * 12

all_bits = []

count_oxy, count_co = 0, 0
gamma = ""
epsilon = ""


with open("input3.txt", "r") as f:
    for line in f:
        bits = [char for char in line.strip("\n")]
        all_bits.append(bits)


oxy = all_bits
co = all_bits

for i in range(12):
    for bit in oxy:
        if bit[i] == "1":
            li[i] += 1
    for bit in co:
        if bit[i] == "1":
            lj[i] += 1

    count_co, count_oxy = len(co), len(oxy)
    
    if li[i] >= count_oxy - li[i]:
        gamma += "1"
    else:
        gamma += "0"

    if len(co) == 1:
        epsilon = "".join(co[0])   
    elif lj[i] >= count_co - lj[i]:
        epsilon += "0"
    else:
        epsilon += "1"

    oxy = [elem for elem in oxy if elem[:i+1] == [char for char in gamma]]
    co = [elem for elem in co if elem[:i+1] == [char for char in epsilon[:i+1]]]

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)

# ans: 2784375
