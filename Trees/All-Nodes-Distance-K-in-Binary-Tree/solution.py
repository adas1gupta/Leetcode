# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque([root])
        adjacency_list = {}

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.val not in adjacency_list:
                    adjacency_list[node.val] = []
                
                if node.left:
                    adjacency_list[node.val].append(node.left.val)
                    queue.append(node.left)
                    
                    if node.left.val not in adjacency_list:
                        adjacency_list[node.left.val] = []
                    adjacency_list[node.left.val].append(node.val)
                
                if node.right:
                    adjacency_list[node.val].append(node.right.val)
                    queue.append(node.right)
                    
                    if node.right.val not in adjacency_list:
                        adjacency_list[node.right.val] = []
                    adjacency_list[node.right.val].append(node.val)
        
        queue = deque([target.val])
        visited = set()
        dist = 0
        res = []

        while queue:
            if dist > k:
                break
            
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)

                if dist == k:
                    res.append(node)
                
                for item in adjacency_list[node]:
                    if item not in visited:
                        queue.append(item)

            dist += 1
        
        return res
