# Leetcode 15 - 3Sum (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/3sum/description/

## Notes: 
 - No need for a set. 
 - Just skip AFTER processing. 
 - Make sure to apply this to both sides (start and end). 
    - Middle doesn't need it because you'll reach the point where there aren't duplicates anymore. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string