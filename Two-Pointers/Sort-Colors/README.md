# Leetcode 75 - Sort Colors (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/sort-colors/description/

## Notes: 
 - Have a left pointer mark the region for where 0s should be.
 - Have a right pointer mark the region for where 2s should be. 
 - Use the middle pointer as a scanner to shift left elements left and right elements right.
 - The problem with using separate if statements instead of using if, elif, else is that you might reach a point where mid is >= right. 
 - This causes a problem because by the time you exceed right, you're supposed to stop processing, but with separate if statements, you keep processing. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string