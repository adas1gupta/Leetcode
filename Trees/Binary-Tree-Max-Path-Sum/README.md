# Leetcode 124 - Binary Tree Maximum Path Sum (Hard)

**Topic**: BFS
**Link**: https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Notes:

# BFS
 - Create a dfs helper.
 - Template is:
    - If not node, return a value. 
    - Compute left and right subtrees. 
    - Combine results. 

 - Apparently, you don't have to include a chain of nodes. 
 - You can just choose as many nodes as you want if they're connected. 
 - So even if something goes down a path, you can just cut off a string of nodes from there. 
 
 - This incentivizes you to just cut off negative numbers. 
 - You might worry about a case like 5 -> 25 -> 10 -> -10 -> 100. 
 - However, the left path at -10 would just be 90 instead of -10. 
 - Only when the cumulative sum is negative would you just cut off the entire thing. 

 - initialize path_sum to be negative infinity. 
 - Compute the maximum sum of the path from left, but make sure that sum is above 0 by simply writing max(0, dfs(node.left))
 - Do the same for right. 
 - Then, compute the path_sum by adding left + right + current_node.val, and see if that beats path_sum. 
 
 - Then, you'd want to return whichever side was the maximum between left or right + the current_node's val. 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 