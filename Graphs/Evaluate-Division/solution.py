class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacency_list = {}
        
        for i, equation in enumerate(equations):
            a, b = equation
            if a not in adjacency_list:
                adjacency_list[a] = []
            adjacency_list[a].append((b, values[i])) # we are appending first / second

            if b not in adjacency_list:
                adjacency_list[b] = []
            adjacency_list[b].append((a, 1 / values[i]))
        
        def dfs(first, second, visited):
            if first not in adjacency_list or second not in adjacency_list:
                return -1
            if first == second: # this is basically c / c
                return 1
            
            visited.add(first)

            for neighbor, weight in adjacency_list[first]:
                if neighbor not in visited:
                    result = dfs(neighbor, second, visited)

                    if result != -1:
                        return weight * result # (first / x) * (x / second) = first / second
            
            return -1 #This is because what can't be determined is given as -1. 
        

        return [dfs(q[0], q[1], set()) for q in queries]