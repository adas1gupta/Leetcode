# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        min_depth = float('inf')
        counter = 1
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if not node.left and not node.right:
                    min_depth = min(min_depth, counter)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            counter += 1
        
        return min_depth
        
