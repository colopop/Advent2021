with open("input.txt") as inp:
    pass

min_x = 117
max_x = 164
min_y = -140
max_y = -89


def shoot(velocity):
    global min_x, max_x, min_y, max_y
    pos = (0,0)
    max_height = 0
    while pos[0] < max_x and pos[1] > min_y:
        #update position
        pos = (pos[0] + velocity[0], pos[1] + velocity[1])

        #update velocity
        velocity = (velocity[0] + (1 if velocity[0] < 0 else 0 if velocity[0] == 0 else -1), velocity[1] - 1)

        #update max height
        if pos[1] > max_height:
            max_height = pos[1]

        #check target area
        if pos[0] >= min_x and pos[0] <= max_x and pos[1] >= min_y and pos[1] <= max_y:
            return True, max_height

    return False, max_height

best_height = 0
for x in range(max_x):
    for y in range(1000):
        shot = shoot((x, y))
        if shot[0] and shot[1] > best_height:
            print((x,y))
            best_height = shot[1]
print(best_height)