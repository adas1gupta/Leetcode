class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(num):
            while num != parents[num]:
                parents[num] = parents[parents[num]] #path compression
                num = parents[num]
            
            return num
        
        def union(a, b):
            first, second = find(a), find(b)

            if first == second: return False

            if ranks[first] > ranks[second]:
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