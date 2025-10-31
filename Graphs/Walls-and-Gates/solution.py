from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        ROWS, COLS = len(rooms), len(rooms[0])
        queue = deque([])
        visited = set()
        
        def add_room(r, c):
            if r < 0 or r >= ROWS:
                return
            elif c < 0 or c >= COLS:
                return
            elif (r, c) in visited:
                return
            elif rooms[r][c] == -1:
                return
            elif rooms[r][c] == 0:
                return 

            visited.add((r, c))
            queue.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                rooms[r][c] = dist

                add_room(r + 1, c)
                add_room(r, c + 1)
                add_room(r - 1, c)
                add_room(r, c - 1)

            dist += 1
