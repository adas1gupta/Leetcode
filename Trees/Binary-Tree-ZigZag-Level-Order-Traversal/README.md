# Leetcode 103 - Binary Tree Zigzag Level Order Traversal (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

## Notes:

# BFS
 - Instead of flipping the queue, just flip the level list.
 - Flipping the queue affects the order in which you add the nodes, which requires you to flip again for the next level. 
    - It just doesn't work.
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 