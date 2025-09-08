# Leetcode 1151 - Minimum Swaps to Group All 1's Together (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/

## Notes: 
 - Lowkey, this was hard.
 - Set up a window of size of the frequency of 1s. 
 - Get the frequency of ones within that window. 
 - Shift the window (left += 1, right += 1) and record the frequency of the 1s in the window as you go. 
 - Record the maximum frequency you see as you shift the window.
 - Then, simply return the frequency of 1s in the entire array - the max frequency you see within a window. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string