# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        cols = {}

        while queue:
            for _ in range(len(queue)):
                node, col = queue.popleft()

                if col not in cols:
                    cols[col] = []
                cols[col].append(node.val)

                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
                
        return [cols[i] for i in sorted(cols.keys())]