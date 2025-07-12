# Leetcode 13 - Roman to Integer (Easy)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/roman-to-integer/description/

## Notes: 
 - Key idea is that Roman integers are ordered from largest to smallest left to right, except for the exceptions mentioned. 
 - Keeping that in mind, the check that you have to make is not if the pair of characters is an exact combination.
 - Rather, it is if left is less than right, which can only happen if an exception is occurring. 
    - If that's the case, just subtract left and add right.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)