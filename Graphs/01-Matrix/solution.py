class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        ROWS, COLS = len(mat), len(mat[0])
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        def bfs(i, j):
            if i >= ROWS or i < 0: return
            if j >= COLS or j < 0: return
            if (i, j) in visited: return

            visited.add((i, j))
            queue.append((i, j))

        level = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                mat[i][j] = level

                bfs(i + 1, j)
                bfs(i - 1, j)
                bfs(i, j + 1)
                bfs(i, j - 1)

            level += 1
        
        return mat