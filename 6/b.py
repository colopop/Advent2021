with open("input.txt") as inp:
    fish = [int(f) for f in inp.readline().split(',')]

fish_today = [0] * (256)
fish_today[0] = len(fish)

spawning_today = [0] * 265
for f in fish:
    spawning_today[f] += 1

for i in range(1, 256):
    fish_today[i] = fish_today[i-1] + spawning_today[i]
    spawning_today[i+7] += spawning_today[i]
    spawning_today[i+9] += spawning_today[i]

print(fish_today[255])