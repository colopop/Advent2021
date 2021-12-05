with open("input.txt") as inp:
    points = set()
    duplicates = set()
    for line in inp:
        line = line.split()
        x1, y1 = line[0].split(',')
        x2, y2 = line[2].split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        x_direction = (x2-x1)//abs(x2-x1) if x1 != x2 else 0
        y_direction = (y2-y1)//abs(y2-y1) if y1 != y2 else 0
        x, y = x1, y1
        while (x,y) != (x2 + x_direction, y2 + y_direction):
            if (x,y) in points:
                duplicates.add((x,y))
            else:
                points.add((x,y))
            x += x_direction
            y += y_direction

    print(len(duplicates))

