class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        ROWS, COLS = len(rooms), len(rooms[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = dist + 1
                        queue.append((nr, nc))
            
            dist += 1