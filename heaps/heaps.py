# In Python, we will use the heapq module
# Note: heapq only implements min heaps
from heapq import *

# Declaration: heapq does not give you a heap data structure.
# You just use a normal list, and heapq provides you with
# methods that can be used on this list to perform heap operations
heap = []

# Add to heap
heappush(heap, 1)
heappush(heap, 2)
heappush(heap, 3)

# Check minimum element
heap[0] # 1

# Pop minimum element
heappop(heap) # 1

# Get size
len(heap) # 2

# Bonus: convert a list to a heap in linear time
nums = [43, 2, 13, 634, 120]
heapify(nums)

# Now, you can use heappush and heappop on nums
# and nums[0] will always be the minimum element

import heapq

# Note: Python's heapq implements a min heap

heap = [67, 341, 234, -67, 12, -976]
heapq.heapify(heap)

heapq.heappush(heap, 7451)
heapq.heappush(heap, -5352)

print(heap)

# The numbers will be printed in sorted order
while heap:
    print(heapq.heappop(heap))