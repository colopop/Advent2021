with open("input.txt") as inp:
    points = set()
    instructions = []
    max_x = 0
    max_y = 0
    read_points = True
    for line in inp.readlines():
        if line == '\n':
            read_points = False
        elif read_points:
            x,y = (int(p) for p in line.strip().split(','))
            if x > max_x:
                max_x = x 
            if y > max_y:
                max_y = y 
            points.add((x,y))
        else:
            instruction = line.strip().split()[2].split('=')
            instructions.append((instruction[0], int(instruction[1])))

for instruction in instructions:
    new_points = set()
    for point in points:
        if instruction[0] == 'x':
            #fold left
            diff = point[0] - instruction[1]
            if diff > 0:
                new_points.add((instruction[1] - diff, point[1]))
            else:
                new_points.add(point)
        elif instruction[0] == 'y':
            #fold left
            diff = point[1] - instruction[1]
            if diff > 0:
                new_points.add((point[0], instruction[1] - diff))
            else:
                new_points.add(point)

    if instruction[0] == 'x':
        max_x = instruction[1]
    else:
        max_y = instruction[1]
    points = new_points

#construct shape
grid = []
for _ in range(max_y+1):
    grid.append([" "] * (max_x+1))

print(grid)
for point in points:
    print(point)
    grid[point[1]][point[0]] = '#'

for row in grid:
    print("".join(row))