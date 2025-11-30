# Leetcode 71 - Simplify Path (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/simplify-path/description/

## Notes: 
 - Use the replace method and get rid of the slashes. 
 - Notice the pattern. 
 - Join the stack and add a / to the beginning. 

## Mistakes:
 - When there are consecutive empty strings, using .split(" ") adds empty strings to the result array

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string