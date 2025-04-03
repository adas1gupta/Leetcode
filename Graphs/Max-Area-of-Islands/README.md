# Leetcode 695 - Max Area of Islands (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/max-area-of-island/description/

## Notes: 
 - Run dfs on every single island, and keep track of the maximum value returned by it. 
 - Have a visited set and a maxArea counter that is initially set to 0. 
 - Define a dfs function
    - It takes in row and col. 
    - Its base cases are if row or col exceeds boundaries or grid[row][col] == 0 or (row, col) are already in visited, then:
        - Return 0
    - Then, add row, col to the visited set.
    - Finally, return 1 + dfs calls in every direction:
        - Row + 1, col
        - Row - 1, col
        - Row, col + 1
        - Row, col - 1
    - Traverse through matrix and if you happen upon a 1, then call the dfs function and compare that result to maxArea.
        - maxArea = max(dfs(row, col), maxArea) 
    - Return maxArea
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(m * n)
- Space: O(m * n)