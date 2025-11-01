class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(i, j):
            if i >= ROWS or i < 0:
                return
            elif j >= COLS or j < 0:
                return
            elif board[i][j] == "T":
                return
            elif board[i][j] == "X":
                return
            
            board[i][j] = "T"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
