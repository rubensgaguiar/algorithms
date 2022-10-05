# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def transversal(self, root, order, index):
        if root == None:
            return order
        
        if len(order) <= index:
            order.append([])

        order[index].append(root.val)
        
        if root.left:
            order = self.transversal(root.left, order, index + 1)
        
        if root.right:
            order = self.transversal(root.right, order, index + 1)

        return order

    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.transversal(root, [], 0)

