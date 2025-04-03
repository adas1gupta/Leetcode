class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(r, c):
            if 0 > r or r >= ROWS:
                return 0
            elif 0 > c or c >= COLS:
                return 0
            elif grid[r][c] == 0:
                return 0
            elif (r, c) in visited:
                return 0
            
            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxArea = max(dfs(row, col), maxArea)
        
        return maxArea