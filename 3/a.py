with open("input.txt") as inp:
    nums = [line.strip() for line in inp]

gamma = 0
epsilon = 0
for idx in range(len(nums[0])):
    ones = 0
    zeros = 0
    for num in nums:
        if num[idx] == '0':
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        gamma += (2 ** (len(nums[0]) - idx - 1))

print(gamma, epsilon, gamma * ((2 ** len(nums[0]) - 1) - gamma))