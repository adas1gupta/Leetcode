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

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string