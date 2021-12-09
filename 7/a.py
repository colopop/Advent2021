with open("input.txt") as inp:
    crabs = [int(c) for c in inp.readline().split(',')]

crabs.sort()

min_cost = 999999999
for i in range(crabs[-1]+1):
    cost = sum(abs(i - c) for c in crabs)
    if cost < min_cost:
        min_cost = cost

print(min_cost)