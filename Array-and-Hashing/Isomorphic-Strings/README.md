# Leetcode 205 - Isomorphic Strings (Easy)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/isomorphic-strings/

## Notes: 
 - Go through the string and as you go, store the count and corresponding character (only once) in the dictionary. 
 - Check if the count is equal and if it's corresponding to the correct character, then keep going.
 - This is O(k) complexity because k is the number of different types of characters that exist. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k)