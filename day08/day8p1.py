total = 0


with open("input.txt", "r") as f:
    for line in f:
        inp, out = line.split(" | ")
        out = out.split()
        for output in out:
            o = len(output)
            if o == 2 or o ==4 or o == 3 or o == 7:
                total += 1

print(total)

