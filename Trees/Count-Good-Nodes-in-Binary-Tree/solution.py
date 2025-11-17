# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node, maximum):
            nonlocal good
            if not node: return
        
            if node.val >= maximum:
                good += 1
            
            dfs(node.left, max(node.val, maximum))
            dfs(node.right, max(node.val, maximum))
        
        dfs(root, root.val)
        return good 
