# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = {}
        queue = deque([(root, 0, 0)])

        while queue:
            for _ in range(len(queue)):
                node, row, col = queue.popleft()

                if col not in cols:
                    cols[col] = []
                cols[col].append((node.val, row))

                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
        
        res = []
        for key in sorted(cols.keys()):
            res.append([x[0] for x in sorted(cols[key], key=lambda x: (x[1], x[0]))])
        
        return res