# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left = p
        right = q
        if p.val > q.val:
            left = q
            right = p

        if root.val >= left.val and root.val <= right.val:
            return root

        if root.val < left.val:
            return self.lowestCommonAncestor(root.right, left, right)

        return self.lowestCommonAncestor(root.left, left, right)
