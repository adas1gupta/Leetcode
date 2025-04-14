# Leetcode 111 - Minimum Depth of Binary Tree (Easy)

**Topic**: BFS, Minimum Depth
**Link**: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

## Notes:

# BFS
 - The reason why we're using bfs here is because you want to stop at the first level where we see a leaf node. 
    - The first level you reach is the answer. 
 - Include the if empty root return ? condition because of queue shenanigans. 
 - Initialize a queue, min_depth, and a counter to keep track of the levels. 
 - While queue, for _ in range(len(queue)), pop the left node. 
    - If it's a leaf node, make the min_depth and counter comparison.
    - If node.left, append left. 
    - If node.right, append right. 
 - Increment the counter after each iteration of the for loop. 
 - Use BFS when you are looking for the shortest path, stop as soon as possible, or track information about a level. 
 - Use DFS when you're accumulating values, exploring entire paths, or backtracking. 
 - BFS for first thing you can find; DFS for best thing you can find. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 