# Leetcode 606 - Construct String from Binary Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/construct-string-from-binary-tree/description/

## Notes:

# BFS
 - Okay, so if there is no left child, but there is a right child, you're supposed to append a pair of parentheses. 
    - Just remember to tag an elif. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 