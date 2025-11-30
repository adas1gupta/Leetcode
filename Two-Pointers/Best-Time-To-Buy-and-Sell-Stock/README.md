# Leetcode 121 - Best Time to Buy and Sell Stock (Easy)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Notes: 
 - Simple enough

 - Just realize that as you traverse through the array, if you find a value smaller than the current value left is pointing at, just set left equal to the index of that value. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string