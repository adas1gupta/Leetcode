# Leetcode 346 - Moving Average from Data Stream (Easy)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/moving-average-from-data-stream/description/

## Notes: 
 - This may be labelled a stack problem, but you should use a queue instead. 
 - Instead of recalculating total by summing the array, simply have a member variable that decrements whenever you remove from the queue and adds whenever you add something to the queue. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string