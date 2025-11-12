# Leetcode 572 - Subtree of Another Tree (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/subtree-of-another-tree/description/

## Notes:

# BFS
 - Use a helper function to check if they are the same tree. 

 - Then, have a function to traverse through until you want to check if they are the same tree. 
 - Then, if not subroot, an empty tree is still a subtree, so return True.
 - However, if not node, then that means you're comparing an empty tree/node to a full subtree, which is obviously False

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 