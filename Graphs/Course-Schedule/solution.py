class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = { i: [] for i in range(numCourses)}

        for course, pre_req in prerequisites:
            adjacency_list[course].append(pre_req)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adjacency_list[course] == []:
                return True
            
            visited.add(course)
            
            for pr in adjacency_list[course]:
                if not dfs(pr):
                    return False
            
            visited.remove(course)
            adjacency_list[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True