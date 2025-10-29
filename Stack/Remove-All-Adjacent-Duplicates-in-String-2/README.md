# Leetcode 1209 - Remove All Adjacent Duplicates in String II (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

## Notes: 
 - Use a stack to build the string. 
 - Go through the string and check if the top of the stack is equal to the character. 
 - If it is, add to the count of said character. 
 - If the count reaches k, pop from the stack. 
    - This is fine because if there are n - k characters left over after the point you're in on the string, those are intended to be kept. 
 - If the character is not the same as the top character, simply append the CHARACTER and the COUNT (which is always 1) to the stack. 

 - Then, just build the string using the stack you have. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string