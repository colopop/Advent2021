with open("input.txt") as inp:
    octopi = []
    for line in inp:
        octopi.append([int(o) for o in line.strip()])

total_flashes = 0
for _ in range(100):

    #increment
    for i, row in enumerate(octopi):
        for j, col in enumerate(row):
            octopi[i][j] += 1
    #flash
    flashing_octopi = set()
    flashed = True
    while flashed:
        flashed = False
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                if octopus > 9 and (i,j) not in flashing_octopi:
                    flashed = True
                    flashing_octopi.add((i,j))
                    if i > 0 and j > 0:
                        octopi[i-1][j-1] += 1
                    if i > 0:
                        octopi[i-1][j] += 1
                    if i > 0 and j < 9:
                        octopi[i-1][j+1] += 1
                    if j > 0:
                        octopi[i][j-1] += 1
                    if j < 9:
                        octopi[i][j+1] += 1
                    if i < 9 and j > 0:
                        octopi[i+1][j-1] += 1
                    if i < 9:
                        octopi[i+1][j] += 1
                    if i < 9 and j < 9:
                        octopi[i+1][j+1] += 1

    #reset octopi
    for pt in flashing_octopi:
        octopi[pt[0]][pt[1]] = 0

    #update flash count
    total_flashes += len(flashing_octopi)

print(total_flashes)