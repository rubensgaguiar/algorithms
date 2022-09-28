from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = defaultdict(lambda: None)
        
        i = 0
        sublist = head
        while sublist != None:
            tmp_val = arr[sublist]
            if sublist == tmp_val:
                return sublist
            arr[sublist] = sublist
            sublist = sublist.next
            i += 1

        return None
