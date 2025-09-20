# Leetcode 224 - Basic Calculator (Hard)

**Topic**: Stack
**Link**: https://leetcode.com/problems/basic-calculator/description/

## Notes: 
 - This is only addition and subtraction, as well as parentheses. 
 - Prioritize the parentheses by using a separate variable to keep track of the sum so far instead of the stack. 
 - Then, use the stack to keep track of the total as you reset it to calculate the value of an expression.
 - Essentially, the algorithm is that you prioritize completing the expressions first and save the state previous to the expression using a stack. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string