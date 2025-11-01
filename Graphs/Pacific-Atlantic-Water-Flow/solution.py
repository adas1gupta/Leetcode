class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited, height):
            if i < 0 or i >= ROWS:
                return
            elif j < 0 or j >= COLS:
                return
            elif (i, j) in visited:
                return
            elif heights[i][j] < height:
                return
            
            visited.add((i, j))
            
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            
            
        for i in range(ROWS):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, COLS - 1, atlantic, heights[i][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        res = []
        
        for item in pacific:
            if item in atlantic:
                res.append(item)
        
        return res
