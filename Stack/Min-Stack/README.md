# Leetcode 155 - Min Stack (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/min-stack/

## Notes: 
 - Use a second stack to keep track of the minimum. 
 - When you pop, make sure to adjust the minimum tracker to be the top of the minimum tracking stack. 
    - If the minimum tracking stack is empty, simply reset to infinity. 
 
 - Just be confident. Utilize a second data structure to keep track of the  minimum. You'll be fine. 

## Mistakes:
 - Don't use a variable to keep track of the minimum because you can pop the minimum but the minimum variable can still be the popped minimum.

 - Instead, to store the minimum, you compare to the top value of the minimum STACK and the value you're appending.


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string