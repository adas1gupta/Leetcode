# Leetcode 1249 - Minimum Remove to Make Valid Parentheses (Medium)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

## Notes: 
 - Use a set to keep track of the indices that are unmatched. 
 - Use a stack to keep track of the indices of open parenthesis. 

 - Basically, if it's an open parenthesis, add THE INDEX to the stack.
 - If we see a close parenthesis, pop from the stack to declare a match. 
    - If there is nothing in the stack, that's when we add it to the set. 
 
 - Then, we go through the stack and see which INDICES of the open parentheses are unmatched and add that to the set. 
 - Then, we just go through the original string and add it to the result string if the index is not in the set. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 