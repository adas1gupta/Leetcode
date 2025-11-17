"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps = {employee.id: employee for employee in employees}
        queue = deque([id])
        total = 0
        #visited = set()

        while queue:
            for _ in range(len(queue)):
                emp = queue.popleft()
                total += emps[emp].importance
                #visited.add(emp)

                for subord in emps[emp].subordinates:
                    #if subord not in visited:
                    queue.append(subord)
        
        return total

