# Leetcode 314 - Binary Tree Vertical Order Traversal (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

## Notes:

# BFS
 - So nodes can line up to be in the same column. 
 - That's why you associate nodes with their column value. 

 - Have the root be at 0. 
 - Columns to the left are appended with the column of the node just popped - 1. 
 - Columns to the right are appended with the column of the node just popped + 1. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 