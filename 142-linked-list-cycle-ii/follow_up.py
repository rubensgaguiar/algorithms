# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        entry = head
        slower = head
        faster = head
        
        if head == None:
            return None

        while faster.next != None and faster.next.next != None:
            slower = slower.next
            faster = faster.next.next

            if slower == faster:
                while slower != entry:
                    slower = slower.next
                    entry = entry.next
                return entry
            

        return None
