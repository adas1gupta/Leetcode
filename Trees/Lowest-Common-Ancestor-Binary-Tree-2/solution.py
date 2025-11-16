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
            if not node: return [False, False]

            left = dfs(node.left)
            right = dfs(node.right)

            found_p = node == p or left[0] or right[0]
            found_q = node == q or left[1] or right[1]

            if found_p and found_q and not lca:
                lca = node
            
            return [found_p, found_q]
        
        dfs(root)
        return lca