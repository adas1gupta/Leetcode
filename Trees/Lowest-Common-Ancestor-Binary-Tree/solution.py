# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def dfs(node):
            nonlocal lca
            if node is None:
                return [False, False]
            
            left = dfs(node.left)
            right = dfs(node.right)

            found_p = right[0] or left[0] or node == p
            found_q = right[1] or left[1] or node == q

            if found_p and found_q and lca is None:
                lca = node
            
            return [found_p, found_q]
        
        dfs(root)
        return lca