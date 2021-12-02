with open("input.txt") as inp:
    route = [(line.split()[0], int(line.split()[1])) for line in inp]

pos = (0,0)
for direction in route:
    if direction[0] == "forward":
        pos = (pos[0] + direction[1], pos[1])
    elif direction[0] == "down":
        pos = (pos[0], pos[1] + direction[1])
    else:
        pos = (pos[0], pos[1] - direction[1])

print(pos, pos[0] * pos[1])