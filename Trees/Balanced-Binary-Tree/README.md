# Leetcode 110 - Balanced Binary Tree (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/balanced-binary-tree/description/

## Notes:

# BFS
 - Create a dfs helper.
 - Template is:
    - If not node, return a value. 
    - Compute left and right subtrees. 
    - Combine results. 

 - Return multiple values (in this case, height and True if the subtree maintains the property)
 - If you ever get a False, then you would want to return False.
 - Call left = dfs(node.left) and right = dfs(node.right) to actually collect the values between the left and right subtrees. 
 - Then, use the return statement to combine information between the two subtrees. 
 
 - The height portion is 1 + the maximum of left or right height.
 - This is because you only care about the maximum because that's the most likely to violate the property. 
 
 - The True portion is checking if the left and right subtree absolute value difference is <= 1, and checking if both left and right subtrees are True. 

 - The space complexity is O(h) because the call/recursion stack is of h height. 
 - h is log n because for a balanced binary tree with n nodes, 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 