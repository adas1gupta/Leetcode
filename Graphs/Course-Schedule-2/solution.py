class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = {c: [] for c in range(numCourses)}

        for res, src in prerequisites:
            adjacency_list[res].append(src)
        
        res = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for pre_req in adjacency_list[course]:
                if dfs(pre_req) == False:
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res