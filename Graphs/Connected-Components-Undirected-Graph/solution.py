class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(num):
            while num != parents[num]:
                # current parent is equal to parent of current parent
                parents[num] = parents[parents[num]] # path compression
                num = parents[num]
            
            return num
        
        def union(a, b):
            first, second = find(a), find(b)

            if first == second: return False

            if ranks[first] > ranks[second]: # combine trees by setting parent of smaller to the parent of larger
            # and adding rank of smaller to the rank of the larger
                parents[second] = first
                ranks[first] += ranks[second]
            else:
                parents[first] = second
                ranks[second] += ranks[first]
            
            return True
        
        res = n
        for a, b in edges:
            if union(a, b) == True:
                res -= 1
        
        return res