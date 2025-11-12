# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            left = same_tree(p.left, q.left)
            right = same_tree(p.right, q.right)

            return left and right and p.val == q.val
        
        def dfs(node):
            if not subRoot:
                return True
            if not node:
                return False
            
            subtree = False
            if node.val == subRoot.val and same_tree(node, subRoot):
                subtree = True
            
            left = dfs(node.left)
            right = dfs(node.right)

            return subtree or left or right
        
        return dfs(root)
