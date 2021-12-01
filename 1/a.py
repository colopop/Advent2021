with open("input.txt") as inp:
    depths = [int(line) for line in inp]
print(sum(depths[i] > depths[i-1] for i in range(1, len(depths))))