# Leetcode 69 - Sqrt (Easy)

**Topic**: Basic Recursion
**Link**: https://leetcode.com/problems/sqrtx/description/

## Notes:

# Recursion 
 - Keep track of the smallest. 
 - In the helper recursive function, take a path string and a node. 
    - This will be similar to the set up from the other tree probblems where you check for one base case, make a change, and check for the next base case (this is especially true in the case of leaf node questions).
    - Prepend the character at the current node to the path string (path = char(node.val) + path)
    - Check if it's a leaf node (no left and no right), and if it is, perform the lexicographic comparison of the current path with the current smallest. 
    - Then, call helper on left and right.
 - Call helper on root and empty string and return smallest. 
 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(logn) -> binary search
- Space: O(logn) -> logn calls 