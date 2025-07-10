# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        res = None

        def dfs(node):
            nonlocal res
            nonlocal k
            if not node or res:
                return 
            
            dfs(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return 
                
            dfs(node.right)
        
        dfs(root)
        return res