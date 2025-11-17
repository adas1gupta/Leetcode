# Leetcode 1457 - Pseudo-Palindromic Paths in a Binary Tree (Medium)

**Topic**: Tree
**Link**: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/

## Notes: 
 - There's that 1 palindrome concept where you can only have at most 1 frequency with an uneven value if the path is of odd length and 0 if even length. 

 - From there, just code it. Break down the code into helpers if need be. 
 
 - There's a more efficient bitmask solution. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) -> explore all the nodes. 
- Space: O(h) -> height of the tree is the amount of space stored for the call stack