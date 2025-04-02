class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set() #can also use a 2D matrix here. 
        islands = 0

        def bfs(row, col):
            queue = deque()
            
            queue.append((row, col))

            while queue:
                r, c = queue.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                
                for direction in directions:
                    calculated_row = r + direction[0]
                    calculated_col = c + direction[1]
                    calculated = (calculated_row, calculated_col)
                    if ((0 <= calculated_row < rows) and 
                        (0 <= calculated_col < cols) and 
                        (grid[calculated_row][calculated_col] == '1') and
                        calculated not in visited):

                        queue.append(calculated)
                        visited.add(calculated)
                visited.add((row, col))
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands