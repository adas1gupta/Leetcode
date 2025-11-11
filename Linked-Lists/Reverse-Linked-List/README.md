# Leetcode 206 - Reverse Linked List (Easy)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/reverse-linked-list/description/

## Notes: 
 - Just use the algorithm of having two pointers at an item and the item ahead of it. 
 - Then, keep a temp of the current item, move the current item forward, have the temp point at the item behind, and move the behind pointer to temp. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 