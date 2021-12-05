with open("input.txt") as inp:
    points = set()
    duplicates = set()
    for line in inp:
        line = line.split()
        x1, y1 = line[0].split(',')
        x2, y2 = line[2].split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if x1 == x2:
            #search vertically
            direction = (y2-y1)//abs(y2-y1)
            for y in range(y1, y2 + direction, direction):
                print(x1, y)
                if (x1, y) in points:
                    duplicates.add((x1, y))
                else:
                    points.add((x1, y))
        elif y1 == y2:
            #search horizontally
            direction = (x2-x1)//abs(x2-x1)
            for x in range(x1, x2 + direction, direction):
                print(x, y1)
                if (x, y1) in points:
                    duplicates.add((x, y1))
                else:
                    points.add((x, y1))
    print(len(duplicates))

