with open("input.txt") as inp:
    crabs = [int(c) for c in inp.readline().split(',')]

print(min(sum(abs(i - c) for c in crabs) for i in range(max(crabs))))