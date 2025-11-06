class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        ranks = [1 for i in range(len(isConnected))]

        #find owners
        def find(num):
            while num != parents[num]:
                parents[num] = parents[parents[num]]
                num = parents[num]
            
            return num
        
        #compare which owners have the larger rank to see which one swallows the other
        def union(first, second):
            one, two = find(first), find(second)

            if one == two: return

            if ranks[one] > ranks[two]:
                parents[two] = parents[one]
                ranks[one] += ranks[two]
            else:
                parents[one] = parents[two]
                ranks[two] += ranks[one]
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        provinces = 0
        for i in range(len(parents)):
            if parents[i] == i:
                provinces += 1

        return provinces