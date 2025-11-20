# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lca = None
        max_depth = 0

        def dfs(node, depth):
            nonlocal lca, max_depth
            if not node: return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            max_depth = max(max_depth, left, right)

            if left == max_depth and right == max_depth:
                lca = node
            
            return max(left, right)
        
        dfs(root, 1)
        return lca