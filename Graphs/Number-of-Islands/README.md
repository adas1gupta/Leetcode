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
        - You can add the current position to the set before or after the processing loop. 
    - To define the bfs, it’s:
        - While the queue is not empty
        - Popleft from the queue. 
        - Define a directions array to list the possible conditions/directions you have to check for (it should contain four items). 
        - Go through the direction array using a for loop and define the row and column to be checked as row + direction[0] and column + direction[1]. 
        - Then, simply check if the calculated rows and columns are between 0 and the ENTIRE rows or columns respectively. 
            - A mistake would be to only check until the passed in (as arguments to the bfs function) rows + 1 and columns + 1. 
            - This is wrong because recursion isn’t being used, so the row and column values wouldn’t be updating.
                - This would cause cases of large islands to be missing, and it would only measure immediate islands to it instead (just the ones directly above/below/left/right to it). 
        - Once you check, just add the calculated row and column matrix position to the queue and the visited set. 
 - Now, finally comes the matrix traversal. Simply traverse and check if the current grid position is equal to one while not being in the visited set.
    - If so, perform bfs, and then, this is where we increment the number of islands by 1.  
 - Return the number of islands. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(m * n)
- Space: O(m * n)