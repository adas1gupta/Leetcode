class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = [set() for i in range(9)]
        COLS = [set() for i in range(9)]
        SUBGRIDS = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                subgrid_ind = j // 3 + (i // 3) * 3
                
                if board[i][j] == ".":
                    continue
                elif board[i][j] in SUBGRIDS[subgrid_ind]:
                    return False    
                elif board[i][j] in ROWS[i]:
                    return False
                elif board[i][j] in COLS[j]:
                    return False
                
                SUBGRIDS[subgrid_ind].add(board[i][j])
                ROWS[i].add(board[i][j])
                COLS[j].add(board[i][j])
        
        return True