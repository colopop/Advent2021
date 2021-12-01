with open("input.txt") as inp:
    depths = [int(line) for line in inp]

# one-liner
print(sum(sum(depths[i-3:i]) > sum(depths[i-4:i-1]) for i in range(4, len(depths))))

# slightly faster
prev = depths[0] + depths[1] + depths[2]
ans = 0
for i, d in enumerate(depths[3:]):
    nxt = prev - depths[i] + d
    if nxt > prev:
        ans += 1
    prev = nxt
print(ans)