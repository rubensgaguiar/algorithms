"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        if root:
            children_list = [root]

            while children_list != []:
                pointer = children_list.pop(0)

                if pointer.children:
                    children_list = pointer.children + children_list

                order.append(pointer.val)

        return order
