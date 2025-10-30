class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(x, y):
            if x >= len(grid):
                return 1
            elif y >= len(grid[0]):
                return 1
            elif x < 0:
                return 1
            elif y < 0:
                return 1
            elif grid[x][y] == 0:
                return 1
            elif (x, y) in visited:
                return 0 
            
            visited.add((x, y))
            perimeter = dfs(x, y + 1)
            perimeter += dfs(x + 1, y)
            perimeter += dfs(x, y - 1)
            perimeter += dfs(x - 1, y)

            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)
