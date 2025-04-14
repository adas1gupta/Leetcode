# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def helper(node, path, current):
            if not node:
                return
            
            path.append(node.val)
            current += node.val
            if not node.left and not node.right:
                if current == targetSum:
                    res.append(copy.copy(path))
                path.pop()
                current -= node.val
                return
            helper(node.left, path, current)
            helper(node.right, path, current)
            path.pop()
            return
        
        helper(root, [], 0)
        return res