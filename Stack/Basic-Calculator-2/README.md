# Leetcode 227 - Basic Calculator II (Medium)

**Topic**: Stack
**Link**: https://leetcode.com/problems/basic-calculator-ii/description/

## Notes: 
 - Pretty fucking hard tbh. Seems like this is a problem that you can only commit to memory. 
 - Have a stack to contain the numbers. 
    - However, be cognizant of how the numbers flow in. 
    - In a test case, you'll usually have "(number)(operation)(number)(operation)(number)", and so on.
    - This means that you won't be processing the last number. 
    - This already implies that you'll have to perform some processing after the loop is done. 
 - Initialize the stack to hold the numbers.
 - Initialize the number holder to contain the current number. 
 - Initialize the operator, which holds the operation before the current operation we reach.
 - This is because the pattern is that when we reach an operation, it's for the number after it.
 - There'll be an operation after the number after the operation we're trying to process so when we reach the next operation is when we process the previous operation.  
 - For the addition operation, simply append the number because we'll be summing at the end.
   - We are also doing this because we don't want to prematurely add before we see a multiplication operation.
   - Same for the subtraction operation. 
 - For multiplication and division, since you haven't sent the current number to the stack, you do stack.pop() (/ or *) curr. 
 - If you don't reach an operator, just update the number you're currently tracking with this piece of code: curr = curr * 10 + int(item)
 - Remember, since you haven't finished processing the last number in the string, you need to perform the operator check one last time after the while loop before you return the sum of the stack. 


 - If you want to not import a truncating library, remember that the // operator truncates toward negative infinity. 
  - The way to get past that is turning both the numbers to their absolute value versions so that they're guaranteed to truncate to 0 instead of -infinity, and then check what the actual division is equal to.
  - Since we're guaranteed that the divisor won't be 0, we can simply divide and check if it's greater than or equal to 0. 
  - If we're not guaranteed that the divisor won't be 0, then we can't divide and instead, we would have to multiply. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string