class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list = {i: [] for i in range(n)}

        for first, second in edges:
            adjacency_list[first].append(second)
            adjacency_list[second].append(first)

        visited = set()

        def dfs(node, prev):
            if node in visited: return False

            visited.add(node)

            for neighbor in adjacency_list[node]:
                if neighbor != prev: 
                    if not dfs(neighbor, node):
                        return False

            return True
        
        return dfs(0, -1) and len(visited) == n
