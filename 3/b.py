with open("input.txt") as inp:
    nums = [line.strip() for line in inp]

def get_rate(options, analysis):
    from statistics import multimode
    for i in range(len(options[0])):
        if len(options) == 1: break
        options = [num for num in options if num[i] == analysis(multimode([o[i] for o in options]))]
    return int(options[0], 2)

print(get_rate(nums, max) * get_rate(nums, lambda x: '0' if max(x) == '1' else '1'))