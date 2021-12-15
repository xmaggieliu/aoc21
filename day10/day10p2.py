total_scores = []


beginning = ["(", "[", "{", "<"]
ending = [")", "]", "}", ">"]

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        incompletes = []
        incomplete = True
        total = 0
        for char in line:
            if char in beginning:
                incompletes.append(char)
            elif not beginning[ending.index(char)] == incompletes[-1]:
                incomplete = False
                break
            else:
                incompletes.pop()
        if incomplete:
            for char in incompletes[::-1]:
                total = total * 5 + beginning.index(char) + 1
            total_scores.append(total)

total_scores.sort()

middle = total_scores[int(len(total_scores) / 2)]
            
print(middle)

