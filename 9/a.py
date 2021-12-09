with open("input.txt") as inp:
    hmap = [[int(i) for i in line.strip()] for line in inp]

total = 0
for i, row in enumerate(hmap):
    for j, cell in enumerate(hmap[i]):
        minimum = (i == 0 or hmap[i-1][j] > hmap[i][j]) and \
                  (i == len(hmap) - 1 or hmap[i+1][j] > hmap[i][j]) and \
                  (j == 0 or hmap[i][j-1] > hmap[i][j]) and \
                  (j == len(hmap[i]) - 1 or hmap[i][j+1] > hmap[i][j])
        risk = 1 + cell
        if minimum:
            total += risk

print(total)