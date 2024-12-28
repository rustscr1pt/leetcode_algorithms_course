# Example 1: 739. Daily Temperatures
#
# Given an array of integers temperatures that represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ithith day to get a warmer temperature. If there is no future day that is warmer, have answer[i] = 0 instead.
#
# The brute force approach would be to iterate over the input, and for each temperature, iterate through the rest of the array until we find a warmer temperature. Let's say we had temperatures = [34, 33, 32, 31, 30, 50]. The first 5 days all share the same "answer" day, the 6th day. Can we leverage this fact to improve from an O(n2)O(n2) time complexity?
#
# The second element 33 is not warmer than the first element 34. The third element 32 is not warmer than the second element 33. This property is transitive, and it implies that the third element is not warmer than the first element (32≯33≯3432≯33≯34). This means there's no point in worrying about the first element until we have found a warmer temperature than the second element because any temperature that isn't warmer than the second element is also not warmer than the first element.
#
# This logic of handling elements in backward order should remind you of a stack. We can push the temperatures onto a stack, and pop them off once we find a warmer temperature. Let's look at another example, temperatures = [40, 35, 32, 37, 50]. Once we get to the 4th element, we have stack = [40, 35, 32]. Now, we see that 37 > 32 and 37 > 35, so we can pop both of them off the stack. This leaves us with stack = [40, 37] after pushing the 37. At the 50, we can pop both elements off the stack because 50 is greater than both of them.
#
# Because the stack is monotonically decreasing, we are guaranteed to pop elements only when we find the first warmer temperature.
#
# The problem wants the distance between elements, so we can store the indices instead of the actual temperatures.
#
# Click here for a more detailed explanation if needed
#
# Recall the problems that we looked at in the "String problems" article. All the problems shared a common theme: elements needed to be "operated" on in some way (verified, deleted, etc.), but not necessarily immediately.
#
# For example, in the problem Valid Parentheses, we needed to verify opening brackets, but not immediately as we saw them. If we had "([{, then the ( needs to wait for the [ to be verified, which needs to wait for the { to be verified.
#
# In the problem Remove All Adjacent Duplicates In String, some characters needed to wait for other characters to be deleted before they could be deleted themselves.
#
# In the problem Backspace String Compare, a character could not be deleted until a character in front of it was deleted first.
#
# We can identify the problem here as well. As mentioned in the explanation above, if you have temperatures = [34, 33, 32, ...], then we know that until we see a day that is warmer than 32, we definitely won't see a day that is warmer than 33 or 34. Thus we can process these days in reverse order.
#
# When we find a temperature that is warmer than 32, we can start moving backward to see if it's warmer than 33 or 34 as well.
#
# Essentially, the stack holds temperatures that we have not yet found a warmer temperature for. Because we are forcing it to be monotonically decreasing, the temperature at the top of the stack will always be the coldest one.
#
# As we iterate, for each temperature curr, we check if curr is warmer than the temperature at the top of the stack. Because we perform this check every iteration, if it is, then curr must be the first day warmer than the day at the top of the stack. We pop from the stack and continue checking the top until the stack is either empty or curr is no longer warmer. Maintaining the monotonic property conveniently has the side effect of processing all the answers.
#
# Because the problem wants the number of days between the temperatures, we need to store the indices instead of the temperatures themselves. But this isn't an issue because given an index we can easily access the temperature from the input.
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)

        return answer




# Example 3: 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# Given an array of integers nums and an integer limit, return the size of the longest subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
#
# The "maximum absolute difference between any two elements" is the maximum element minus the minimum element. The question is asking for the longest subarray and has a constraint on the subarray - max - min <= limit. We learned that these characteristics suggest using a sliding window.
#
# We also just learned how to keep the maximum element in a sliding window in the previous example. We need to do that again here but also keep the minimum element.
#
# Use two deques - one monotonic increasing and one monotonic decreasing. The monotonic increasing one has the minimum element in the window at the first index. The monotonic decreasing one has the maximum element in the window at the first index. Then, we can use the same sliding window format we learned in the arrays and strings chapter. Add elements to the deques from the right, remove them from the left when the max - min > limit, and make sure to maintain the deques at each iteration.
#
# Recall that the formula for the length of a window is right - left + 1.
#
# Click here for a more detailed explanation if needed
#
# We can identify this as a sliding window problem. The constraint metric is the maximum element in the window minus the minimum element in the window. The numeric restriction is <= limit.
#
# In the previous example we kept a monotonic decreasing data structure that only contained elements in the current window. This meant that the maximum element in the window was always the first element in the data structure.
#
# If we instead had a monotonic increasing data structure, then the minimum element in the window will always be the first element in the data structure.
#
# We also learned in the previous example that when the data structures are monotonic, then we can easily find the next maximum element when the maximum was removed from the window. The exact same logic applies for the minimum.
#
# Now that we know how to maintain the maximum and minimum elements in a window, we can just apply the standard sliding window algorithm: add elements from the right, remove them from the left whenever the constraint is broken. As we add and remove elements, we need to maintain our monotonic data structures.


from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        left = ans = 0

        for right in range(len(nums)):
            # maintain the monotonic deques
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()

            increasing.append(nums[right])
            decreasing.append(nums[right])

            # maintain window property
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans