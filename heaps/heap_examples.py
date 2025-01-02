# Example 1: 1046. Last Stone Weight
#
# You are given an array of integers stones where stones[i] is the weight of the ithith stone. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. If x == y, then both stones are destroyed. If x != y, then x is destroyed and y loses x weight. Return the weight of the last remaining stone, or 0 if there are no stones left.
#
# In this problem, we need to repeatedly find the 2 maximum elements. Let's convert stones into a max heap, so that we can pop the two maximum elements in O(log⁡n)O(logn), perform the smash and then re-add to the heap (if the stones aren't both destroyed) in O(log⁡n)O(logn). We can continue the process until there are one or zero stones left.

# To solve this problem, we can just simulate the process. The problem is, it could be expensive to repeatedly find the two heaviest stones. Just sorting the input descending and going through the elements in order wouldn't work because often, a smash results in a new stone that is put back into the input.
#
# With a heap, we can remove the two maximum elements in logarithmic time. After we perform the smash, if we have a leftover stone, we can add it back in logarithmic time. Note that logarithmic time is much faster than linear time, so this is a huge improvement over using a normal array.
#
# So we put all the stones into a max heap. Then we just simulate the process until there are one or zero stones remaining. Pop the 2 max elements and then apply the rules in the problem description.
#
# Don't focus on what's happening under the hood - just remember what a heap can do for you and how to use the operations.

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) # turns an array into a heap in linear time
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        return -stones[0] if stones else 0



# Python's heap implementation only implements min heaps. To simulate a max heap, we can just make all values we put on the heap negative.
#
# On each smash, at least one rock is destroyed, so there can be at most n iterations. At each iteration, we perform pops and pushes on the heap, which has a length of n at the start. This gives us a time complexity of O(n⋅log⁡n)O(n⋅logn). The heap uses O(n)O(n) space. Note that in Python we are re-using the input, so we should count it towards the space complexity, which we wouldn't normally do.



# Example 2: 2208. Minimum Operations to Halve Array Sum
#
# You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. Return the minimum number of operations to reduce the sum of nums by at least half.
#
# What is the best way to choose numbers to halve? We want to minimize the steps, so we want to maximize the amount we reduce nums by at each step. This means at any given moment, we should choose the largest element. To track the largest element at any given time, let's convert the input into a max heap. At each step, we pop the maximum x off, remove x / 2 from the sum, and then push x / 2 back onto the heap.
#
# This is another great example of when to use a heap - we need to find the max element repeatedly. Like in the previous example, it's not enough to just sort the input descending and go through the elements in order, because elements are added back in after being halved.
#
# First, we convert the input into a heap. Then we define target as the sum of the elements divided by two - this is the amount of reduction we need to achieve.
#
# Now, while target > 0, we need to reduce the sum. Remove the maximum element x from the heap (which is fast and easy). Reduce it to x / 2 by subtracting x / 2 from target, and then put x / 2 back into the heap.
#
# The heap will always give us the maximum element in logarithmic time, even as we add elements back in.

import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        heap = [-num for num in nums]
        heapq.heapify(heap)

        ans = 0
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x / 2)

        return ans

# As you can see from the previous two examples, a heap is an amazing data structure when you need to repeatedly find the maximum or minimum element. It can handle insertions and removals all while maintaining the max/min property, all in logarithmic time.
#
# Each iteration of the loop takes O(log⁡n)O(logn) time from the heap operations. The number of operations needed is linear with n. While you may be thinking: if we have a huge number, it would need to be halved many times. True, but each operation on it would also reduce the sum by a large amount. This gives us a time complexity of O(n⋅log⁡n)O(n⋅logn).
#
# A more clear argument as to why the number of operations is bounded by n - you could always just perform the operation on each number once.
