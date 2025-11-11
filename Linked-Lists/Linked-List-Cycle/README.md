# Leetcode 141 - Linked List Cycle (Easy)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/linked-list-cycle/description/

## Notes: 
 - Use the fast and slow pattern.
 - Start both from head and move fast twice as fast. 
 - If slow ever = fast, there's a cycle.
 
 - If it ends, return True. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 