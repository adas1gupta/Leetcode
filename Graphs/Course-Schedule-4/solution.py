class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjacency_list = { i: [] for i in range(numCourses)}
        for prereq, course in prerequisites:
            adjacency_list[course].append(prereq)
        
        def dfs(course):
            if course in indirect:
                return indirect[course]
            
            indirect[course] = set()
            for prereq in adjacency_list[course]:
                indirects = dfs(prereq)
                indirect[course].add(prereq)
                
                for item in indirects:
                    indirect[course].add(item)

            return indirect[course]

        indirect = {}

        for course in range(numCourses):
            dfs(course)

        res = []

        for u, v in queries:
            res.append(u in indirect[v])
        
        return res