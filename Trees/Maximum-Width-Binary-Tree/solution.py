# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        max_width = 0

        while queue:
            min_index = float('inf')
            max_index = float('-inf')
            for _ in range(len(queue)):
                node, index = queue.popleft()

                min_index = min(min_index, index)
                max_index = max(max_index, index)

                max_width = max(max_width, max_index - min_index + 1)

                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, (index * 2) + 1))
                
        return max_width
