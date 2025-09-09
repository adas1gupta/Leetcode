# Leetcode 150 - Evaluate Reverse Polish Notation (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

## Notes: 
 - Stack for the numbers. 
 - The pattern is that once you reach the operation, you process first two numbers. 
 - Tricky part is understanding what truncates towards 0 means. 
    - It means that -0.5 or 1.5 always goes down to 0 or 1, respectively.
    - Just use the math.trunc function and do second / first instead of second // first. 
    - No need to convert the result to an integer first. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string