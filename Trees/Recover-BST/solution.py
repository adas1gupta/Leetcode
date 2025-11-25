# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None

        def dfs(node):
            nonlocal first, second, prev
            if not node: return
        
            dfs(node.left)

            if prev and node.val < prev.val:
                if not first:
                    first = prev
            
            if prev and first and node.val < prev.val:
                second = node

            prev = node
            dfs(node.right)
        
        dfs(root)
        first.val, second.val = second.val, first.val

        return root