class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        ranks = [1 for i in range(n + 1)]

        def find(num):
            while num != parents[num]:
                parents[num] = parents[parents[num]]
                num = parents[num]
            
            return num
        
        def union(a, b):
            one, two = find(a), find(b)
            if one == two: return True

            if ranks[one] > ranks[two]:
                ranks[one] += ranks[two]
                parents[two] = one
            
            else:
                ranks[two] += ranks[one]
                parents[one] = two
            
            return False
        
        edge = None

        for first, second in edges:
            if union(first, second):
                edge = [first, second]
        
        return edge