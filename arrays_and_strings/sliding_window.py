# To summarize what each variable does in the code:
#
#     left: the leftmost index of our current window
#     right: the rightmost index of our current window
#     current: the sum of our current window
#     answer: the length of the longest valid window we have seen so far
#
# Iterate right over the input to add elements to the window. Update curr by adding nums[right] to it. When the window becomes invalid (curr > k), remove elements from the window by subtracting nums[left] from curr. Then increment left. We need to do this until the window becomes valid again, so we use a while loop.
#
# The size of a window is right - left + 1. Update our answer only when the window becomes valid.

def find_length(nums : list[int], k : int) -> int:
    left = current = answer = 0
    for right in range(len(nums)):
        current += nums[right]
        while current > k:
            current -= nums[left]
            left += 1
        answer = max(answer, right - left + 1)
    return answer



answer = find_length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)
print(answer) #4


# Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?
#
# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
#
# Because the string can only contain "1" and "0", another way to look at this problem is "what is the longest substring that contains at most one "0"?". This makes it easy for us to solve with a sliding window where our condition is window.count("0") <= 1. We can use an integer curr that keeps track of how many "0" we currently have in our window.
#
# Click here for a more detailed explanation if needed
#
# The input can only contain "1" or "0". We want to find the max consecutive "1". Because any element that isn't a "1" is a "0", this problem is equivalent to "what is the longest substring with at most one "0", since we could just flip that "0" and it's guaranteed every other character in the substring would be a "1".
#
# Notice that the problem is asking for the length of a substring, and also has defined what makes a substring valid. The constraint metric is "how many 0s are in the substring". The numeric restriction is <= 1. Therefore, if we use an integer curr to track the constraint metric, the condition to determine if a window is valid is curr <= 1.
#
# We can use the exact same process as in the previous example now. We iterate over the elements with a pointer right. At each element, if s[right] is equal to "1", we don't need to do anything. If it's equal to "0", we increment curr.
#
# Whenever the window becomes invalid (curr > 1), we remove elements from the left. If s[left] == "0", then we can decrement curr. We increment left to remove elements.
#
# Again, the size of a window is right - left + 1. We update our answer with this value after the while loop because the window is guaranteed to be valid.


def find_length(string: str) -> int:
    left = current = answer = 0
    for right in range(len(string)):
        if string[right] == '0':
            current += 1
        while current > 1:
            if string[left] == '0':
                current -= 1
            left += 1
        answer = max(answer, right - left + 1)
    return answer


answer = find_length("1101100111")
print(answer) #5





# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
#
# As we mentioned before, we can build a window of length k and then slide it along the array. Add and remove one element at a time to make sure the window stays size k. If we are adding the value at i, then we need to remove the value at i - k.
#
# After we build the first window we initialize our answer to curr to consider the first window's sum.


def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)

    return ans



# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted
#
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: Maximum
# average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
# Input: nums = [5], k = 1
# Output: 5.00000

from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    current = 0
    for index in range(k):
        current += nums[index]
    answer = current / k
    for index in range(k, len(nums)):
        current += nums[index]
        current -= nums[index - k]
        if current / k > answer:
            answer = current / k
    return answer


print(findMaxAverage([5], 1))

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    left = answer = zero_holder = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_holder += 1
        while zero_holder > k:
            if nums[left] == 0:
                zero_holder -= 1
            left += 1
        answer = max(answer, right - left + 1)
    return answer



print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3))