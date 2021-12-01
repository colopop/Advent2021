with open("input.txt") as inp:
    depths = [int(line) for line in inp]

prev = depths[0]
ans = 0
for d in depths[1:]:
    if d > prev:
        ans += 1
    prev = d

print(ans)