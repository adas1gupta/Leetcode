# Leetcode 623 - Add One Row to Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/add-one-row-to-tree/description/

## Notes:

# BFS
 - This is easy to get off by one errors. Just make sure to keep track of levels and if the levels variable is at the value where you actually want to make the insertion/change. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 