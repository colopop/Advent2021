with open("input.txt") as inp:
    pass

min_x = 117
max_x = 164
min_y = -140
max_y = -89


def shoot(velocity):
    global min_x, max_x, min_y, max_y
    pos = (0,0)
    while pos[0] < max_x and pos[1] > min_y:
        #update position
        pos = (pos[0] + velocity[0], pos[1] + velocity[1])

        #update velocity
        velocity = (velocity[0] + (1 if velocity[0] < 0 else 0 if velocity[0] == 0 else -1), velocity[1] - 1)

        #check target area
        if pos[0] >= min_x and pos[0] <= max_x and pos[1] >= min_y and pos[1] <= max_y:
            return True

    return False

winning_shots = 0
for x in range(max_x+1):
    for y in range(min_y,-min_y+1):
        if shoot((x, y)):
            winning_shots += 1

print(winning_shots)
