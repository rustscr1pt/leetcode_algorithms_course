# Example 2: 2270. Number of Ways to Split Array
#
# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.
#
# A brute force approach would be to iterate over each index i from 0 until nums.length - 1. For each index, iterate from 0 to i to find the sum of the left section, and then iterate from i + 1 until the end of the array to find the sum of the right section. This algorithm would have a time complexity of O(n2)O(n2).
#
# If we build a prefix sum first, then iterate over each index, we can calculate the sums of the left and right sections in O(1)O(1), which would improve the time complexity to O(n)O(n).
#
# When we split the array into two parts, we are left with two adjacent subarrays. We need to find the sums of these subarrays and compare them.
#
# There are n−1n−1 ways to split the array (the right section can't be empty). For each of these splits, it would cost O(n)O(n) to iterate over the two subarrays and find their sums.
#
# Instead, we can spend O(n)O(n) once to build a prefix sum before trying any splits. Then we can use the prefix sum to perform each of the n−1n−1 splits in O(1)O(1) time. As we know, with a prefix sum we can calculate the sum of any subarray in O(1)O(1).
#
# Let's say we are splitting at index i. The left section has all elements in the array up to index i, so it has a sum of prefix[i]. The right section begins at index i + 1 and ends at the final index n - 1. This means it has a sum of prefix[n - 1] - prefix[i].
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        ans = 0
        for i in range(n - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans


# # Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# #
# # Return the running sum of nums.
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

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



# Given an array of integers nums, you start with an initial positive value startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.
#
# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2
#
# Input: nums = [1,2]
# Output: 1
# Explanation: Minimum start value should be positive.
#
# Input: nums = [1,-2,-3]
# Output: 5

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

