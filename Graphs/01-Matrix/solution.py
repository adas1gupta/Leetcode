class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        queue = deque([])
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
        
        def bfs(i, j, dis):
            if i >= ROWS or i < 0: return
            if j >= COLS or j < 0: return
            if (i, j) in visited: return
            if mat[i][j] == 0: return

            visited.add((i, j))

            mat[i][j] = dis

            queue.append((i, j, dis))
        
        while queue:
            for _ in range(len(queue)):
                x, y, dist = queue.popleft()

                bfs(x + 1, y, dist + 1)
                bfs(x - 1, y, dist + 1)
                bfs(x, y + 1, dist + 1)
                bfs(x, y - 1, dist + 1)
        
        return mat