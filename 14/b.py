with open("input.txt") as inp:
    polymer = inp.readline().strip()
    inp.readline()
    rules = { a : b for a, b in [line.strip().split(' -> ') for line in inp.readlines()]}

from collections import Counter

def update_polymer(base, rules, frequencies):
    new_poly = Counter()
    for pair in base:
        if pair in rules:
            new_poly[pair[0] + rules[pair]] += base[pair]
            new_poly[rules[pair] + pair[1]] += base[pair]
            frequencies[rules[pair]] += base[pair]
        else:
            new_poly[pair] += base[pair]
    return new_poly

#update format of polymer to { pair : # of occurrences }
new_poly = Counter()
frequencies = Counter()
for i in range(1, len(polymer)):
    new_poly[polymer[i-1:i+1]] += 1
    frequencies[polymer[i]] += 1
polymer = new_poly

for _ in range(40):
    polymer = update_polymer(polymer, rules, frequencies)

#meta analysis
mode = max(frequencies, key=lambda x: frequencies[x])
antimode = min(frequencies, key=lambda x: frequencies[x])
print(frequencies[mode] - frequencies[antimode])