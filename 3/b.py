with open("input.txt") as inp:
    nums = [line.strip() for line in inp]

def most_common(nums, idx):
    ones = 0
    zeros = 0
    for num in nums:
        if num[idx] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        return '1'
    else:
        return '0'

def least_common(nums, idx):
    ones = 0
    zeros = 0
    for num in nums:
        if num[idx] == '0':
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        return '0'
    else:
        return '1'

oxy_rating = nums[:]
i = 0
while len(oxy_rating) > 1 and i < len(nums[0]):
    oxy_rating = [num for num in oxy_rating if num[i] == most_common(oxy_rating, i)]
    i += 1
oxy_rate = int(oxy_rating[0], 2)
print(oxy_rating)

co2_rating = nums[:]
i = 0
while len(co2_rating) > 1 and i < len(nums[0]):
    co2_rating = [num for num in co2_rating if num[i] == least_common(co2_rating, i)]
    i += 1
co2_rate = int(co2_rating[0], 2)
print(co2_rating)

print(oxy_rate * co2_rate)