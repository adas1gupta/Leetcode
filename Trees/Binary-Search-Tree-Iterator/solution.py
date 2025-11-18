# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._dfs(root) #Fill with all left elements initially

    def _dfs(self, node):
        while node:
            self.stack.append(node)
            node = node.left
            
    def next(self) -> int:
        top = self.stack.pop() # there's guaranteed to be an element here
                               # because next is supposed to be valid
                               # Given that there's guaranteed to be an element
                               # We can pop off from the stack
                               # This will be inorder because we fill the stack
                               # With the leftmost value, then we pop off the root
                               # and we check if the root has any right elements
                               # before we return root. 
                               # If there is, append right so that right will be on top
                               # In that way, we'll have returned Left -> Root -> Right
        if top.right:
            self._dfs(top.right)
        
        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()