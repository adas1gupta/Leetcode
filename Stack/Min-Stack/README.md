# Leetcode 155 - Min Stack (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/min-stack/

## Notes: 
 - Use a second stack to keep track of the minimum. 
 - When you pop, make sure to adjust the minimum tracker to be the top of the minimum tracking stack. 
    - If the minimum tracking stack is empty, simply reset to infinity. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string