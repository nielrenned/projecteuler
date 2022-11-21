from utilities import pentagonal

def solve():
    nums = [pentagonal(n) for n in range(1,10000)]
    nums_set = set(nums)
    for i in range(len(nums)):
        for j in range(i):
            p1 = nums[i]
            p2 = nums[j]
            if (p1 + p2) in nums_set and (p1 - p2) in nums_set:
                return abs(p1-p2)