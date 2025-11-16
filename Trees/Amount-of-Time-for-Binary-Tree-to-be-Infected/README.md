# Leetcode 2385 - Amount of Time for Binary Tree to Be Infected (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

## Notes:

# BFS
 - Turn the tree into a graph using an adjacency list and a queue to go through the tree. 

 - Then, start from the starting node and bfs through the graph. 
    - Keep a visited set to not go through a cycle
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 