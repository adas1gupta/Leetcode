# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 'r')])
        total = 0

        while queue:
            for _ in range(len(queue)):
                node, status = queue.popleft()
                if not node.left and not node.right and status == 'l':
                    total += node.val
                if node.left:
                    queue.append((node.left, 'l'))
                if node.right:
                    queue.append((node.right, 'r'))
        
        return total
                