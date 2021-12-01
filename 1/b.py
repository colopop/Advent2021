with open("input.txt") as inp:
    depths = [int(line) for line in inp]

first = depths[0]
second = depths[1]
third = depths[2]
ans = 0
for d in depths[3:]:
    tmp = first + second + third
    if tmp - first + d > tmp:
        ans += 1
    first = second
    second = third
    third = d

print(ans)