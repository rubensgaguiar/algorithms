# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verifyConditions(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.val <= root.left.val or root.right and root.val >= root.right.val:
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if self.verifyConditions(root):
            if root.left and not self.isValidBST(root.left) or \
                root.right and not self.isValidBST(root.right):
                return False

            return True
