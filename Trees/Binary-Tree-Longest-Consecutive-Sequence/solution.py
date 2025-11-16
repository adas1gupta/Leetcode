# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_length = 0

        def dfs(node, prev, length):
            nonlocal max_length
            if not node: return
            
            if node.val == prev + 1:
                length += 1
            else:
                length = 1
            
            max_length = max(max_length, length)

            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)
        
        dfs(root, root.val - 1, 0)
        return max_length