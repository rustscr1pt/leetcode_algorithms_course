# Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
#
# For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.

# The most elegant solution comes from using the fast and slow pointer technique. If we have one pointer moving twice as fast as the other, then by the time it reaches the end, the slow pointer will be halfway through since it is moving at half the speed.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Get the middle value
middle_value = get_middle(head)
print("Middle value:", middle_value)  # Output: Middle value: 3


# Given the head of a linked list, determine if the linked list has a cycle.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

# If a linked list has a cycle, you can imagine some group of nodes forming a circle, and traversal never ends as it moves around that circle infinitely. One way to try to solve this problem would be to just iterate through the list for an arbitrarily large amount of iterations. If there isn't a cycle, then we will eventually reach the end of the list. If there is a cycle, then we will never reach an end and after a huge amount of iterations, we can conclude that there is probably a cycle.
#
# The problem with this approach is that it isn't an actual general solution. What if there is no cycle, but there just happens to be more nodes than the iteration cutoff? If we increase the iteration cutoff, we can always argue that we could pass in a longer linked list. If we make the cutoff too large, it becomes impractical, and we are hard coding which is a terrible practice.
#
# The better approach is to use a fast and slow pointer. Imagine a straight racetrack (like the one used in the 100m sprint). If two runners of significantly different speeds are racing, then the slower one will never catch up to the faster one. The faster runner finishing the race is like the fast pointer reaching the end of the linked list.
#
# But what if the runners were instead running around a circular racetrack, and needed to complete many laps? In that case, the faster runner will eventually pass (lap) the slower runner.
#
# We can apply this logic - move a fast pointer twice the speed of a slow pointer. If they ever meet (except at the start), then we know there must be a cycle. If the fast pointer reaches the end of the linked list, then there isn't a cycle.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(hasCycle(head))