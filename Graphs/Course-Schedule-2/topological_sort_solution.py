class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = {n: [] for n in range(numCourses)}

        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses
        res = []

        def dfs(n):
            if state[n] == VISITED:
                return True
            if state[n] == VISITING:
                return False

            state[n] = VISITING

            for item in adjacency_list[n]:
                if not dfs(item):
                    return False
                
            res.append(n)
            state[n] = VISITED
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res