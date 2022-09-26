from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def recursive(self, head, next):
        if next == None:
            return head

        new_head = ListNode()
        new_head.next = head
        new_head.val = next.val

        next = next.next

        return self.recursive(new_head, next)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive(None, head)
