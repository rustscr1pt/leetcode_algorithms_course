from typing import List


def runningSum(nums: List[int]) -> List[int]:
    if len(nums) > 0:
        prefix = [nums[0]]
        for index in range(1, len(nums)):
            prefix.append(nums[index] + prefix[index - 1])
        return prefix
    else:
        return []

print(runningSum([3,1,2,10,1]))