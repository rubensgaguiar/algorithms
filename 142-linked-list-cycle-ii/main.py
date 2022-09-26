# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 1
        sublist = head.next

        while sublist != None:
            tmp_head = head
            for i in range(c):
                if tmp_head == sublist:
                    return i

                tmp_head = tmp_head.next

            c += 1
            sublist = sublist.next

        return -1
