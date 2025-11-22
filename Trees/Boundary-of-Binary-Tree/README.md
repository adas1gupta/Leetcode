# Leetcode 545 - Boundary of Binary Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/boundary-of-binary-tree/description/

## Notes:
 - Create 3 functions to collect left boundary, then leaves, then right. 
 - There will be overlap in terms of collecting leaf nodes so simply return if the node is a leaf for the left and right functions. 

 - Root will overlap if you call the three functions on root, so just call left on root.left, leaves on root, and right on root.right and initialize the answer array with root


 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 