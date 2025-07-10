# Leetcode 101 - Symmetric Tree (Easy)

**Topic**: Recursion
**Link**: https://leetcode.com/problems/symmetric-tree/description/

## Notes:
 - Create a helper function to take in two arguments since the original function only takes in one. 
    - Check if both p and q are None. If they are, then it's the base case, and you should return True because they're both None. 
    - Then, check if one of them is None and the other isn't. If that's the case, return False. 
    - Finally, return if p.val is equal to q.val and return the helper call on p.left and q.left and p.right and q.right. 
 - Then, call helper on root and root. 
 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(h) -> The call stack is O(h) because recursion goes down a path. 