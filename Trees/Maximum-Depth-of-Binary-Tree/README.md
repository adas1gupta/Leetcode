# Leetcode 104 - Maximum Depth of Binary Tree (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

## Notes:

# BFS
 - Create a dfs helper.
 - Template is:
    - If not node, return a value. 
    - Compute left and right subtrees. 
    - Combine results. 

 - Here, you're grabbing the height of the left subtree and right subtree. 
 - Then, how that node combines results from left and right subtree is by returning the maximum between the two.
    - That's how results are combined: the return value. 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 