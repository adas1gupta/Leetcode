# Leetcode 209 - Minimum Size Subarray Sum (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/minimum-size-subarray-sum/description/

## Notes: 
 - Pretty simple: just make sure to use a while loop to avoid control flow issues. 
 - While total is greater than or equal to target, decrement what left was pointing to from the total and increment left. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string