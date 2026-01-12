# Leetcode 542 - 01 Matrix (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/01-matrix/description/

## Notes: 
 - This is Multi-source BFS. 

 - The trick here is to start from 0s instead of 1s (similar to walls and gates). 
    - For the 0s, since the level will be 0, the 0s will correctly be set to 0.

 - Don't include a check to return the moment you encounter a 1. 
    - That prevents you from exploring further 1s. 

 - You can modify original matrix or have another matrix to store the results. It doesn't matter. 

## Mistakes:
 - Need to use a visited set because cells that get updated to 1 will be added in again, thereby overwriting their distances.


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)