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