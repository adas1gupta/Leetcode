# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        copy = root

        while copy:
            if copy.val == val:
                return copy
            elif copy.val < val:
                copy = copy.right
            else:
                copy = copy.left
        
        return None