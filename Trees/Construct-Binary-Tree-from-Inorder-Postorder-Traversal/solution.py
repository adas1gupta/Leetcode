# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val_to_ind = {inorder[i]: i for i in range(len(inorder))}
        ind = len(postorder) - 1

        def dfs(left, right):
            nonlocal ind
            if left > right: return None

            val = postorder[ind]
            ind -= 1

            mid = val_to_ind[val]
            node = TreeNode(val)

            node.right = dfs(mid + 1, right)
            node.left = dfs(left, mid - 1)

            return node
        
        return dfs(0, len(inorder) - 1)