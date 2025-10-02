# Leetcode 224 - Basic Calculator (Hard)

**Topic**: Stack
**Link**: https://leetcode.com/problems/basic-calculator/description/

## Notes: 
 - This is only addition and subtraction, as well as parentheses. 
 - Prioritize the parentheses by using a separate variable to keep track of the sum so far instead of the stack. 
 - Then, use the stack to keep track of the total as you reset it to calculate the value of an expression.
 - Essentially, the algorithm is that you prioritize completing the expressions first and save the state previous to the expression using a stack. 
    - Clean the string. 
    - Use total to keep track of the sum of the expression and curr to keep track of the current number. 
    - When you encounter an opening parenthesis, append the current total and sign of the expression to the stack. 
    - Reset total and curr. Curr cannot be a coefficient of an expression here. 
    - Important to reset the sign to default just like how sign was default at the very beginning. 
    - This is because we don't want to encounter a positive 6 and then subtract it because the previous sign was negative. 
    - If you encounter a closing parenthesis, first add curr to the total for the mini-expression. 
    - Then, update total by using the sign in the stack and applying it to the total of the expression and adding the total that was appended to the stack. 
    - Reset the sign to the default because if a negative sign preceded the expression, it was already evaluated, so when you encounter new numbers, you want the default. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string