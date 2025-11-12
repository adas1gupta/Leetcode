# Leetcode 112 - Path Sum (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

## Notes:

# BFS
 - New pattern unlocked. 
 - If there is anything that involves leaf nodes, use the base cases of if not node: do x and then if not node.left and not node.right: perform x. 

 - If not node, return False because that isn't a valid path from root to leaf. 
 - If not node.right and not node.left, that is a root node, so add the current node's val (that will be the root node), and check if it's equal to target. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 