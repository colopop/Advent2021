with open("input.txt") as inp:
    nums = [line.strip() for line in inp]

gamma = sum(2 ** (len(nums[0]) - 1 - i) for i in range(len(nums[0])) if [num[i] for num in nums].count('1') > (len(nums) // 2))
print(gamma * (2 ** len(nums[0]) - 1 - gamma))