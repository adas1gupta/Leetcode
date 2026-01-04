# Leetcode 394 - Decode String (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/decode-string/description/

## Notes: 
 - Use stack to keep track of the current string and its count. 
 - What you'll encounter first is count. 
    - Then parenthesis, then string. 
    - Essentially, the formula here is previous list you have built + current list.
 - First thing you'll see is a number, and it'll be pushed onto the stack with no list because there is no previous list to build upon. 
    - Then, you see a parenthesis, and you'll push the previous list and the current number onto the stack while resetting the current_list.
    - Then, you'll build current_list, and if you encounter another parenthesis, you'll push the current_list and the number you are guaranteed to encounter if you see another opening parenthesis. 
    - If you see a closing parenthesis, you pop the number and previous list off, then multiply the current_list with the number and add that to the previous_list you popped off. 
 - Then, perform the O(n) join at the end. 

 2nd Reattempt:
 - Just add one level to the string. 
 - After you encounter the closing parenthesis, compute current level and pop previous level and rebuild the string. 
 - The rebuild is necessary probably because the combined string itself can be multiplied (nested levels). 

## Mistakes:
 - Stack should only store state.
 - Current_list should only store the actual characters.


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string