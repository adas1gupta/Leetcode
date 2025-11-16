# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        queue = deque([root])
        levels = 1 

        if depth == 1:
            return TreeNode(val, root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if levels == depth - 1:
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val, None, node.right)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels += 1
        
        return root