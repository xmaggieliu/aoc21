cards = []
card = []

# value n = n'th number called from nums
marked = []
mark = []

num_for_bingo = []
bingo_in_row = []
bingo_in_col = []


with open("input4.txt", "r") as f:
    nums = list(map(int, f.readline().split(",")))
    fd = f.readlines() 

fd = [list(map(int, line.split())) for line in fd]
# DEL empty line
fd.pop(0)
# add empty to the end
fd.append([])

for line in fd:
    if len(line) != 0:
        card.append(line)
        m = [nums.index(num) + 1 for num in line]
        mark.append(m)
        bingo_in_row.append(max(m))
    else:
        cards.append(card)
        marked.append(mark)

        for i in range(5):
            # i is col num, j is row num
            bingo_col = 0
            for j in range(5):
                bingo_col = max(bingo_col, mark[j][i])
            bingo_in_col.append(bingo_col)

        first_row = min(bingo_in_row)
        first_col = min(bingo_in_col)

        num_for_bingo.append(min(first_col, first_row))

        card = []
        mark = []
        bingo_in_row = []
        bingo_in_col = []

first_win = max(num_for_bingo)
b_card = num_for_bingo.index(first_win)
sum_uncalled = 0
max_called = 0

for i in range(5):
    for j in range(5):
        if marked[b_card][i][j] > first_win:
            sum_uncalled += cards[b_card][i][j]
        elif marked[b_card][i][j] == first_win:
            max_called = cards[b_card][i][j]

total_score = max_called * sum_uncalled
print(total_score)

