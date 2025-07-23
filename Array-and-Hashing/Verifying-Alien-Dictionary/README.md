# Leetcode 953 - Verifying an Alien Dictionary (Easy)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/verifying-an-alien-dictionary/description/

## Notes: 
 - Hash the order by making (char, order) pairs. 
 - Two pointer on pairs of words starting from the beginning. 
 - Create a word pointer and go through each word until one is done. 
    - If first letter is greater than the other, return False.
    - If equal, continue comparing.
    - If not, then break.
 - Then, check for the edge case where both were equal until the second word was done. 
    - If the second word was done before the first, then the first should be ahead lexicographically, so return False. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n log k)
- Space: O(1)