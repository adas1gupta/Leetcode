class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = {}
        for after, before in prerequisites:
            if after not in adjacency_list:
                adjacency_list[after] = []
            adjacency_list[after].append(before)
        
        visited, cycle = set(), set()
        res = []
        def dfs(node):
            if node in cycle: return False
            if node in visited: return True
            if node not in adjacency_list: 
                res.append(node)
                visited.add(node)
                return True
            
            cycle.add(node)

            for neighbor in adjacency_list[node]:
                if not dfs(neighbor): return False
                
            cycle.remove(node)
            res.append(node)            
            visited.add(node)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return res
