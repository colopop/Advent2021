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


new_points = set()
for point in points:
    if instructions[0][0] == 'x':
        #fold left
        diff = point[0] - instructions[0][1]
        if diff > 0:
            new_points.add((instructions[0][1] - diff, point[1]))
        else:
            new_points.add(point)
    elif instruction[0] == 'y':
        #fold left
        diff = point[1] - instructions[0][1]
        if diff > 0:
            new_points.add((point[0], instructions[0][1] - diff))
        else:
            new_points.add(point)

print(len(new_points))