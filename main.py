from typing import List


def runningSum(nums: List[int]) -> List[int]:
    if len(nums) > 0:
        prefix = [nums[0]]
        for index in range(1, len(nums)):
            prefix.append(nums[index] + prefix[index - 1])
        return prefix
    else:
        return []


def minStartValue(nums: List[int]) -> int:
    if len(nums) > 0:
        memo = nums[0]
        prefix = [nums[0]]
        for index in range(1, len(nums)):
            calculated = nums[index] + prefix[index - 1]
            prefix.append(calculated)
            if calculated < memo:
                memo = calculated
        print(prefix)
        if memo > 0:
            return 1
        else:
            return abs(memo) + 1
    else:
        return 0


print(minStartValue([2,3,5,-5,-1]))