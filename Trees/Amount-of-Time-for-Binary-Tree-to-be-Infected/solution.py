# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacency_list = {}
        queue = deque([root])
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.val not in adjacency_list:
                    adjacency_list[node.val] = []
                
                if node.left:
                    if node.left.val not in adjacency_list:
                        adjacency_list[node.left.val] = []
                    adjacency_list[node.left.val].append(node.val)
                    adjacency_list[node.val].append(node.left.val)

                    queue.append(node.left)

                if node.right:
                    if node.right.val not in adjacency_list:
                        adjacency_list[node.right.val] = []
                    adjacency_list[node.right.val].append(node.val)
                    adjacency_list[node.val].append(node.right.val)

                    queue.append(node.right)
        
        queue = deque([start])
        visited = set()
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)

                for item in adjacency_list[node]:
                    if item not in visited:
                        queue.append(item)
            
            minutes += 1
        
        return minutes - 1