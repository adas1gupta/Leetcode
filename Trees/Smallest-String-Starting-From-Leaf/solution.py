# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        total = []
        
        def helper(node, path):
            if not node:
                return 
            
            path += f"{node.val}->"
            
            if not node.left and not node.right:
                end = path.rstrip("->")
                total.append(end)
                return 
            
            helper(node.left, path)
            helper(node.right, path)
        
        helper(root, "")
        return total