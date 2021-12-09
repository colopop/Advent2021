with open("input.txt") as inp:
    signals = []
    for line in inp:
        digits, code = line.split('|')
        digits = [set(d) for d in digits.split()]
        code = [set(c) for c in code.split()]
        signals.append((digits, code))

total = 0
for digits, code in signals:
    encoding = [None] * 10
    for digit in digits:
        if len(digit) == 2:
            encoding[1] = digit
        elif len(digit) == 3:
            encoding[7] = digit
        elif len(digit) == 4:
            encoding[4] = digit
        elif len(digit) == 7:
            encoding[8] = digit

    #deduce the rest with set operations
    mid_left_corner = encoding[4] - encoding[1]
    for digit in digits:
        if len(digit) == 5:
            if mid_left_corner.issubset(digit):
                encoding[5] = digit
    cross_diagonals = encoding[8] - encoding[5]
    for digit in digits:
        if len(digit) == 5:
            if cross_diagonals.issubset(digit):
                encoding[2] = digit

    encoding[9] = encoding[1] | encoding[5]
    encoding[6] = (encoding[8] - encoding[9]) | encoding[5]
    encoding[3] = (encoding[9] & encoding[2]) | encoding[1]
    encoding[0] = encoding[8] - (encoding[2] & encoding[4] & encoding[5])

    #now get the number
    for i, d in enumerate(code):
        for k, c in enumerate(encoding):
            if d == c:
                total += 10 ** (3-i) * k
                break

print(total)