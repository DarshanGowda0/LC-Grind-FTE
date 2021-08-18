# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(node):
            if not node:
                return
            left = recur(node.right)
            right = recur(node.left)
            node.left = left
            node.right = right
            
            return node
        
        return recur(root)