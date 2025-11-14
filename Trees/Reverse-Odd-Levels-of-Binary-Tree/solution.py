# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        levels = 0

        while queue:
            right = 0
            nodes = list(queue)
            if levels % 2 == 1:
                r = len(queue) - 1

                i = 0
                n = len(queue) 
                
                while i <= r:
                    nodes[i].val, nodes[r].val = nodes[r].val, nodes[i].val

                    i += 1
                    r -= 1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels += 1
        
        return root