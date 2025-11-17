# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first = []
        second = []

        def dfs(node, arr):
            if not node: return

            if not node.left and not node.right:
                arr.append(node.val)
            
            dfs(node.left, arr)
            dfs(node.right, arr)
        
        dfs(root1, first)
        dfs(root2, second)

        if len(first) != len(second):
            return False
        
        for i in range(len(first)):
            if first[i] != second[i]:
                return False
        
        return True