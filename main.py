from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    array = []
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    while slow:
        print(slow.val)
        array.append(slow.val)
        slow = slow.next
    return array

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

print(middleNode(head))