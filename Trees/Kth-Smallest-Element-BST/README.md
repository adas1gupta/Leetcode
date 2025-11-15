# Leetcode 230 - Kth Smallest Element in a BST (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

## Notes:

# BFS
 - Keep a nonlocal count and answer.
 - Return if not node or answer already found. 

 - Do inorder traversal and increment count before you check count. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 