# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # create a mirror tree
        # compare if both trees are same
        
        def mirrorTree(node):
            if not node:
                return None
            
            newNode = TreeNode(node.val)
            newNode.left = mirrorTree(node.right)
            newNode.right = mirrorTree(node.left)
            
            return newNode
        
        def compareTree(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            return node1.val == node2.val and compareTree(node1.left, node2.left) and compareTree(node1.right, node2.right)

        
        newTree = mirrorTree(root)
        return compareTree(root, newTree)