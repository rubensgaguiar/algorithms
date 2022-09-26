import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head

        cm = 0
        ch = 0
        while head != None:
            if math.ceil(ch / 2) > cm:
                middle = middle.next
                cm += 1

            head = head.next
            ch += 1

        return middle


