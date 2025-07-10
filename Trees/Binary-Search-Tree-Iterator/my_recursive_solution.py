# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.lst = []
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return 
        
        self.lst.append(node)
        self.dfs(node.left)
        
        if not self.lst:
            self.dfs(node.right)

        return

    def next(self) -> int:
        to_return = self.lst.pop()
        if to_return and to_return.right:
            self.dfs(to_return.right)

        return to_return.val

    def hasNext(self) -> bool:
        if not self.lst:
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()