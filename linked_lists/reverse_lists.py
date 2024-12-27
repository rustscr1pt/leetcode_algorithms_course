class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # first, make sure we don't lose the next node
        curr.next = prev  # reverse the direction of the pointer
        prev = curr  # set the current node to prev for the next node
        curr = next_node  # move on

    return prev

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

print(reverse_list(head))