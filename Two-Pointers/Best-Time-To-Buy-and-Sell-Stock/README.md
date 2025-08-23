# Leetcode 121 - Best Time to Buy and Sell Stock (Easy)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Notes: 
 - This is a sorted array. 
 - Have one pointer serve as the scanner and the other as the anchor. 
 - Scan the elements from the start, and if the count of the element that the scanner is on is <= 2, then set anchor equal to scanner and increment hold. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string