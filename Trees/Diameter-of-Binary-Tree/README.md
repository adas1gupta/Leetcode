# Leetcode 543 - Diameter of Binary Tree (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/diameter-of-binary-tree/description/

## Notes:

# BFS
 - Create a dfs helper.
 - Template is:
    - If not node, return a value. 
    - Compute left and right subtrees. 
    - Combine results. 

 - Keep a global diameter value.

 - You want to compute the height of left and right and sum them and compare them to current diameter. 
 - Then, you want to send back up the maximum of the subtree instead of the combined sum because sending up the combined sum yields to incorrect values. 
 

# Mistakes

 - It's not left + right - 1 because when you do 1 + dfs(node.X), it's 1 edge to left AND 1 edge to right.
 - Left to node is 1 edge and right to node is another edge so left + right would be 2 edges here instead of left + right - 1. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 