total = 0

with open("input.txt", "r") as f:
    translator = [""] * 10
    for line in f:
        inp, out = line.split(" | ")
        inp = ["".join(sorted(num)) for num in inp.strip().split()]
        inp = sorted(inp, key=len)
        out = ["".join(sorted(num)) for num in out.strip().split()]
        for input in inp:
            o = len(input)
            if o == 2:
                translator[1] = input
            elif o == 4:
                translator[4] = input
            elif o == 3:
                translator[7] = input
            elif o == 7:
                translator[8] = input
            elif o == 5 and all(c in input for c in translator[7]):
                translator[3] = input
            elif o == 6 and all(c in input for c in translator[4]):
                translator[9] = input
            elif o == 6 and all(c in input for c in translator[1]):
                translator[0] = input
            elif o == 6:
                translator[6] = input
            elif all(ch in input for ch in [c for c in translator[4] if not c in translator[1]]):
                translator[5] = input
            else:
                translator[2] = input
        
        number = ""

        for num in out:
            number += str(translator.index(num))
        total += int(number)

print(total)

# 996280