class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        queue = deque([(sr, sc)])
        ROWS, COLS = len(image), len(image[0])
        visited = set()
        visited.add((sr, sc))
        image[sr][sc] = color

        def bfs(i, j):
            if i >= ROWS or i < 0: return
            if j >= COLS or j < 0: return
            if (i, j) in visited: return
            if image[i][j] != original: return

            visited.add((i, j)) 
            queue.append((i, j))
            image[i][j] = color

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                bfs(i + 1, j)
                bfs(i - 1, j)
                bfs(i, j + 1)
                bfs(i, j - 1)
        
        return image