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


# Example 3: Given the head of a linked list and an integer k, return the kthkth node from the end.
#
# For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.

# This problem is very similar to the first example. Again, we could just convert the list to an array, or we could iterate through once to find the length and then iterate again once we know the length, but there is a more elegant solution.
#
# If we separate the two pointers by a gap of k, and then move them at the same speed, they will always be k apart. When the fast pointer (the one further ahead) reaches the end, then the slow pointer must be at the desired node, since it is k nodes behind.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(find_node(head, 2))