# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        palindromes = 0
        freq = {}

        def traverse_dict(even):
            counter = 0
            if even:
                for val in freq.values():
                    if val % 2 == 1:
                        return False
            else:
                for val in freq.values():
                    if val % 2 == 1:
                        counter += 1
                    if counter > 1:
                        return False
            
            return True

        def dfs(node):
            nonlocal palindromes
            if not node: return

            freq[node.val] = freq.get(node.val, 0) + 1

            if not node.left and not node.right:
                palindromic = False
                if sum(freq.values()) % 2 == 0:
                    palindromic = traverse_dict(True)
                else:
                    palindromic = traverse_dict(False)        

                if palindromic:
                    palindromes += 1
            
            dfs(node.left)
            dfs(node.right)
            
            freq[node.val] -= 1

        dfs(root)
        return palindromes