# Leetcode 726 - Number of Atoms (Hard)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/number-of-atoms/description/

## Notes: 
 - Have a stack of dictionaries. 
 - Every time you see an open parenthesis, append a new dictionary to the stack to represent the next level. 
 - If it's closed, collect the coefficient of the parentheses to multiply the counts within stack[-1]'s dictionary. 
    - Pop the dictionary from the stack and collect its elements and count to add to the next stack[-1]'s dictionary. 
 - Otherwise, collect the element and count in 1 go and update the top dictionary in the stack. 
 - Then, just build the result. 


 - 'OH' isn't a singular element, so make sure to parse correctly by checking if the element is a lowercase letter

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 