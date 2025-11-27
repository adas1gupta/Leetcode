"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        clones = {}

        def dfs(root):
            if root in clones: return clones[root]

            if root not in clones:
                clones[root] = Node(root.val)
            
            for neighbor in root.neighbors:
                clones[root].neighbors.append(dfs(neighbor))
            
            return clones[root]
        
        return dfs(node)