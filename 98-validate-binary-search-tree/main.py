# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verifyConditions(self, root: Optional[TreeNode], maximum, minimum) -> bool:
        invalid_conditions = root.left and root.val <= root.left.val or \
            root.right and root.val >= root.right.val or \
            maximum and root.val >= maximum or \
            minimum and root.val <= minimum

        return not invalid_conditions

    
    def validateBST(self, root: Optional[TreeNode], maximum=None, minimum=None):
        if self.verifyConditions(root, maximum, minimum):
            invalid_bst = root.left and not self.validateBST(root.left, maximum=root.val, minimum=minimum) or \
                root.right and not self.validateBST(root.right, maximum=maximum, minimum=root.val)

            return not invalid_bst

        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root)
