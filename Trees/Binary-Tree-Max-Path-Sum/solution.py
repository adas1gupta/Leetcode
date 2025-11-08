# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sum = float('-inf')

        def dfs(node):
            nonlocal path_sum
            if not node:
                return 0
            
            left = node.val + max(0, dfs(node.left))
            right = node.val + max(0, dfs(node.right))
            path_sum = max(path_sum, left + right - (node.val))

            return max(left, right)
        
        dfs(root)
        return path_sum