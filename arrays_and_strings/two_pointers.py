
# Example 1: Given a string s, return true if it is a palindrome, false otherwise.
#
# A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True



#
# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
#
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        # curr is the current sum
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False



# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        starting_point = 0
        end_point = len(s) - 1
        while starting_point < end_point:
            s[starting_point], s[end_point] = s[end_point], s[starting_point]
            starting_point += 1
            end_point -= 1