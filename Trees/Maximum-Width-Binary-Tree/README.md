# Leetcode 662 - Maximum Width of Binary Tree (Medium)

**Topic**: BFS
**Link**: https://leetcode.com/problems/maximum-width-of-binary-tree/description/

## Notes:

# BFS
 - Only trick to realize here is that the left and right children are the index of the parent * 2 and * 2 + 1, respectively. 
 - Use BFS because it's interested in maximum difference between nodes on a level basis. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 