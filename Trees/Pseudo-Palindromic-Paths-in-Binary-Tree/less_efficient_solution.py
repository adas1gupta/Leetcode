# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        paths = 0
        freq = {}

        def palindromic():
            even = False
            if sum(freq.values()) % 2 == 0:
                even = True
            
            counter = 0
            for val in freq.values():
                if val % 2 == 1:
                    counter += 1
                
                if (even and counter > 0) or counter > 1:
                    return False
            
            return True

        def dfs(node):
            nonlocal paths
            if not node: return
            
            freq[node.val] = freq.get(node.val, 0) + 1
            
            if not node.left and not node.right:
                if palindromic():
                    paths += 1
            
            dfs(node.left)
            dfs(node.right)

            freq[node.val] -= 1

        dfs(root)
        return paths
