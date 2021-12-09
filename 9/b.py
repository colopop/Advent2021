with open("input.txt") as inp:
    hmap = [[int(i) for i in line.strip()] for line in inp]

#collect low points, since each basin has exactly one
low_points = {}
for i, row in enumerate(hmap):
    for j, cell in enumerate(hmap[i]):
        minimum = (i == 0 or hmap[i-1][j] > hmap[i][j]) and \
                  (i == len(hmap) - 1 or hmap[i+1][j] > hmap[i][j]) and \
                  (j == 0 or hmap[i][j-1] > hmap[i][j]) and \
                  (j == len(hmap[i]) - 1 or hmap[i][j+1] > hmap[i][j])
        if minimum:
            low_points[(i,j)] = None

#dfs starting at each low point to determine size of basin
for point in low_points:
    stack = [point]
    visited = set()
    while len(stack) > 0:
        row, col = stack.pop()
        if row != 0 and (row-1, col) not in visited and hmap[row-1][col] != 9:
            stack.append((row-1, col))
        if row != len(hmap) - 1 and (row+1, col) not in visited and hmap[row+1][col] != 9:
            stack.append((row+1, col))
        if col != 0 and (row, col-1) not in visited and hmap[row][col-1] != 9:
            stack.append((row, col-1))
        if col != len(hmap[row]) - 1 and (row, col+1) not in visited and hmap[row][col+1] != 9:
            stack.append((row, col+1))
        visited.add((row, col))
    low_points[point] = len(visited)

top3 = [b[1] for b in sorted(low_points.items(), reverse=True, key=lambda x: x[1])[:3]]
print(top3[0] * top3[1] * top3[2])