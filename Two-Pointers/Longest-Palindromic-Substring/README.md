# Leetcode 5 - Longest Palindromic Substring (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/longest-palindromic-substring/description/

## Notes: 
 - The idea is to start from the middle and expand outwards. 
 - There's two types of test cases: even palindrome and odd palindrome. 
 - Odd palindrome is where you have two pointers start from one character, and then increment/decrement them and keep doing that until they reach a point where they don't equal each other anymore. 
 - Even palindrome is where you have one pointer start at one character and the other pointer start at the character next to it, and keep incrementing/decrementing each other until they don't equal each other anymore. 
 - Then, simply compare the lengths of the palindrome and take the longest one. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string