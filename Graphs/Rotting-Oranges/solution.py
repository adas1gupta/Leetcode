from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque([])
        fresh_fruit = 0
        fresh_to_rotten = 0

        def traverse(r, c):
            nonlocal fresh_to_rotten
            if r >= ROWS or r < 0:
                return
            elif c >= COLS or c < 0:
                return
            elif (r, c) in visited:
                return
            elif fresh_to_rotten == fresh_fruit:
                return
            
            visited.add((r, c))
            

            if grid[r][c] == 1:
                queue.append([r, c])
                fresh_to_rotten += 1
                

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh_fruit += 1
                
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                traverse(x + 1, y)
                traverse(x, y + 1)
                traverse(x - 1, y)
                traverse(x, y - 1)

            minutes += 1
        
        if fresh_fruit != fresh_to_rotten:
            return -1
        elif fresh_fruit == 0:
            return 0
        else:
            return minutes - 1
