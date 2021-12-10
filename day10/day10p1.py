syntax_score = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
total = 0


beginning = ["(", "[", "{", "<"]
ending = [")", "]", "}", ">"]

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        incompletes = []
        for char in line:
            if char in beginning:
                incompletes.append(char)
            elif not beginning[ending.index(char)] == incompletes[-1]:
                total += syntax_score[char]
                break
            else:
                incompletes.pop()
            
print(total)

