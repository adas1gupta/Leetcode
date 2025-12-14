# Leetcode 909 - Snakes and Ladders (Medium)

**Topic**: Graphs, DFS
**Link**: https://leetcode.com/problems/snakes-and-ladders/description/

## Notes:
 - The algorithm involves using BFS to calculate the possible paths from each point.
    - Each point will roll x from 1 to 6.
 - This is still O(m * n) time complexity because you are simply just collecting points, not paths.
 - You will still be putting the points you've visited in a visited set.

 - Store the position and number of moves into a queue.
 - Keep a visited set and store the positions you've visited.

 - Pop the position and number of moves from the set.
    - If you're at the position ROWS * COLS, then return moves.
 - Go through the dice from 1 to 6 and calculate the next position.
 - First, you have to check if the next position you calculated exceeds ROWS * COLS.
    - That's because you'll potentially get an index out of bounds error later.
 - Then, calculate the row and column before adjusting the row from top down.
    - This is because you have to alternate the column based on the row index from the bottom.
 - Adjust col if need be and adjust row so that you can access it from the top down (bottom up is 2nd row from bottom so 1, but there's actually 5 rows so 4 - 1, so row 3)
 - Adjust next position if there's a ladder.
 - Add next position if it hasn't already been calculated yet (aka in visited), and add it to the queue with moves += 1


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)