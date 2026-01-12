class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        ROWS, COLS = len(mat), len(mat[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + x, dc + y

                    if 0 <= nr < ROWS and 0 <= nc < COLS and mat[nr][nc] == 1 and (nr, nc) not in visited:
                        mat[nr][nc] = mat[x][y] + 1
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        return mat