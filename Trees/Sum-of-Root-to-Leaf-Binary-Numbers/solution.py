# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def helper(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                nonlocal total
                total += int(path, 2)
                return
            
            helper(node.left, path)
            helper(node.right, path)
            return
        
        helper(root, "")
        return total