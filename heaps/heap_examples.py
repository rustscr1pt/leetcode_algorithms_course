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

