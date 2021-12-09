with open("input.txt") as inp:
    signals = []
    codes = []
    for line in inp:
        signal, output = line.split('|')
        signal = signal.split()
        output = output.split()
        signals.append(signal)
        codes.extend(output)

print(codes)
print(sum(1 for x in codes if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7 ))
