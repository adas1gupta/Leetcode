# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}

        def dfs(node):
            if not node: return -1

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)

            height = max(left, right)

            if height not in levels:
                levels[height] = []
            levels[height].append(node.val)

            return max(left, right)
        
        dfs(root)
        return [levels[i] for i in sorted(levels.keys())]