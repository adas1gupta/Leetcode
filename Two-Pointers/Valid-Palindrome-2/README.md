# Leetcode 680 - Valid Palindrome 2 (Easy)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/valid-palindrome-ii/description/

## Notes: 
 - Start from the ends and compare. 
 - If you reach a point where it starts to differ, you need to check both test cases:
    - One where if you shift the left pointer, and remove the previous left character, you'll achieve a palindrome. 
    - One where if you shift the right pointer, and remove the previous right character, you'll achieve a palindrome. 
 - Check for either case, and if either is true, return True, and if both are False, return False. 
 - Don't try and calculate the ranges yourself ([range:range:]). Just create a string and use [::-1].
 - If you spot no mismatches, return True because it says at most one character. 
 - Also, if you use string splicing, it creates new objects, so it's better to create a helper to check instead of creating new objects and comparing if the splice and its reverse are equal after spotting a mismatch. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string