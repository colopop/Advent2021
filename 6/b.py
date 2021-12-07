with open("input.txt") as inp:
    fish = [int(f) for f in inp.readline().split(',')]

spawning_today = [0] * 9
for f in fish:
    spawning_today[f] += 1

fish_yesterday = len(fish)
for _ in range(256):
    fish_today = fish_yesterday + spawning_today[0]
    spawning_today[7] += spawning_today[0]
    spawning_today.append(spawning_today[0])
    fish_yesterday = fish_today
    spawning_today.pop(0)

print(fish_today)