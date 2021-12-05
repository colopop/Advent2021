with open("input.txt") as inp:
    segments = [(int(line.split()[0].split(',')[0]), int(line.split()[0].split(',')[1]), 
                 int(line.split()[2].split(',')[0]), int(line.split()[2].split(',')[1])) for line in inp]

points = set()
duplicates = set()
for x1, y1, x2, y2 in segments:
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