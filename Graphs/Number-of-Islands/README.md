# Leetcode 200 - Number of Islands (Medium)

**Topic**: Graphs, BFS 
**Link**: https://leetcode.com/problems/number-of-islands/description/

## Notes: 
 - The number of islands can be visualized as levels of diagonals, indicating BFS because it’s a level-based traversal algorithm. 
 - The first step is setting up the traversal of the matrix. The traversal of the matrix requires rows and cols for the nested for loop. 
 - Have a visited set and the result for the number of islands. 
 - Define a bfs helper function that takes in a row and column, and uses bfs to go through the matrix from the given starting point of an island. 
    - Within the bfs helper function, define the queue and use the outer scope visited set. 
    - Add the current position in the matrix to that set and append the current position to the queue. 
        - This is to start the queue for processing. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(m * n)
- Space: O(m * n)