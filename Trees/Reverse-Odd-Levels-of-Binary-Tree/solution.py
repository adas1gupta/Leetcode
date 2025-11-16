# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])

        levels = 0
        while queue:
            if levels % 2 == 1:
                nodes = list(queue)
                i, n = 0, len(nodes) - 1

                while i <= n:
                    nodes[i].val, nodes[n].val = nodes[n].val, nodes[i].val

                    i += 1
                    n -= 1
                
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels += 1
        
        return root