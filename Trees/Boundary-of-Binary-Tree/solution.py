# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]

        def left(node):
            if not node: return
            if not node.left and not node.right: return

            res.append(node.val)
            left(node.left)
            if not node.left:
                left(node.right)
        
        def leaves(node):
            if not node: return

            if not node.left and not node.right: 
                res.append(node.val)
                return 
            
            leaves(node.left)
            leaves(node.right)
        
        def right(node):
            if not node: return
            if not node.left and not node.right: return

            right(node.right)
            if not node.right:
                right(node.left)

            res.append(node.val)

        if not root.left and not root.right:
            return res

        left(root.left)
        leaves(root)
        right(root.right)

        return res