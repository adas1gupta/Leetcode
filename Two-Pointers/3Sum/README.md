# Leetcode 15 - 3Sum (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/3sum/description/

## Notes: 
 - No need for a set. 
 - Just skip AFTER processing. 
 - Make sure to apply this to both sides (start and end). 
    - Middle doesn't need it because you'll reach the point where there aren't duplicates anymore. 

 - Don't duplicate check outside of triplets because you'll reach a test case where you increment j because sum < 0.
 - Then, you check if k is equal to the number it just processed, and since it is, k will decrement 1 even though you want to hold k in place. 

 - The reason why it works for duplicates is because you move both j and k, so they shouldn't be equal to their previous values. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string