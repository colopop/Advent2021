with open("input.txt") as inp:
    polymer = inp.readline().strip()
    inp.readline()
    rules = { a : b for a, b in [line.strip().split(' -> ') for line in inp.readlines()]}

def update_polymer(base, rules):
    new_polymer = [base[0]]
    for i in range(1, len(base)):
        if base[i-1:i+1] in rules:
            new_polymer.append(rules[base[i-1:i+1]])
        new_polymer.append(base[i])
    return "".join(new_polymer)

for _ in range(40):
    polymer = update_polymer(polymer, rules)

#meta analysis
frequencies = { a : polymer.count(a) for a in set(polymer)}
mode = max(frequencies, key=lambda x: frequencies[x])
antimode = min(frequencies, key=lambda x: frequencies[x])

print(polymer.count(mode) - polymer.count(antimode))