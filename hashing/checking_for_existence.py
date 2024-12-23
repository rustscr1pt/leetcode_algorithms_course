#
# Example 1: 1. Two Sum
#
# Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

# We are looking for two numbers that sum to target. We iterate over the input and for each element num, we see if this element can be paired with another number to form target.
#
# If another element target - num exists, then their sum num + target - num = target is what we are looking for.
#
# So as we iterate over the input, we put elements in a hash map. Then in the future, we can check if we've seen target - num for each num in O(1)O(1). The problem wants us to return the indices instead of the numbers themselves, so we can associate each number with its index.

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:  # This operation is O(1)!
            return [i, dic[complement]]

        dic[num] = i

    return [-1, -1]


# Example 2: 2351. First Letter to Appear Twice
#
# Given a string s, return the first character to appear twice. It is guaranteed that the input will have a duplicate character.
# The brute force solution would be to iterate along the string, and for each character c, iterate again up to c to see if there is any match.
# This improves our time complexity to O(n)O(n) as each for loop iteration now runs in constant time.
#
# The space complexity is a more interesting topic of discussion. Many people will argue that the space complexity is O(1)O(1) because the input can only have characters from the English alphabet, which is bounded by a constant (26). This is very common with string problems and technically correct. In an interview setting, this is probably a safe answer, but you should also note that the space complexity could be O(m)O(m), where mm is the number of allowable characters in the input. This is a more general answer and also technically correct.

def repeatedCharacter(self, s: str) -> str:
    for i in range(len(s)):
        c = s[i]
        for j in range(i):
            if s[j] == c:
                return c
        return ""


# Example 3: Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
# We can solve this in a straightforward manner - just iterate through nums and check if x + 1 or x - 1 is in nums. By converting nums into a set beforehand, these checks will cost O(1)O(1).
#
# Converting the input into a set beforehand is another example of pre-processing.
# Because the checks are O(1)O(1), the time complexity is O(n)O(n) since each for loop iteration runs in constant time. The set will occupy O(n)O(n) space.

def find_numbers(nums):
    ans = []
    nums = set(nums)

    for num in nums:
        if (num + 1 not in nums) and (num - 1 not in nums):
            ans.append(num)

    return ans

