# Leetcode 18 - 4Sum (Medium)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Notes: 
 - skip duplicates for i and j
 - Once you get to k and l, you have to check if they're equal to target OR less/greater than target. 
 - The key part to remember is that you are incrementing pointers based on if it's less than or greater than target and not if they match or don't match. 
 - If it's less than, increment k, and if it's greater than, decrement l. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string