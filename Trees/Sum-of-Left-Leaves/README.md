# Leetcode 404 - Sum of Left Leaves (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/sum-of-left-leaves/description/

## Notes:

# BFS
 - Using bfs here because we're not necessarily interested in the path here. We're more so interested in seeing if the node is a left leaf, and there's other ways of detecting that. 
 - Since we're using bfs, include the standard if not root base case. 
 - Initialize a queue with the [(root, 'r')] where 'r' is used to indicate if the node is a left or right leaf. 
 - Have a total variable. 
 - Set up the queue stuff. 
    - Pop node and status.
    - Check if it's a leaf node and if it's status is left.
    - If it is, add to total. 
    - If there's a left node, add it to the queue with a left status.
    - If there's a right node, add it to the queue with a right status. 
 - Return total. 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> O(n) in the worst case
         O(2^h) -> in the average case where the tree is balanced. This is where h is equal to the (last_level - first_level), otherwise known as (last_level - 1). For example if there are 4 levels, the height is 3. This is amortized to O(n).  
         O(1) in the best case where the tree is skewed. 
