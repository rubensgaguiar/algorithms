"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def build_list(self, root: 'Node', order: List[int]) -> List[int]:
        order.append(root.val)
        if root.children:
            for child in root.children:
                order = self.build_list(child, order)
        return order

    def preorder(self, root: 'Node') -> List[int]:
        if root:
            return self.build_list(root, [])
        return []
