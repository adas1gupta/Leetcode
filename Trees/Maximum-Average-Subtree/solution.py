# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maximum_avg = 0

        def dfs(node):
            nonlocal maximum_avg
            if not node: return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            total_nodes = left[1] + right[1] + 1
            total = left[0] + right[0] + node.val

            maximum_avg = max(maximum_avg, total / total_nodes)

            return [total, total_nodes]
        
        dfs(root)
        return maximum_avg
