# Leetcode 83 - Remove Duplicates from Sorted List (Easy)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## Notes: 
 - Whatever has a .something (.next or .val) needs to be in the while loop. 
 - Whatever is before the last .something NEEDS TO BE IN THE WHILE LOOP CONDITION. 

 - There's no need for a set here because this is in order. 
 - Just have the second pointer start ahead of head.
    - Since we're starting at head.next, we have to check if there is head or head.next ([] or [1]) and return head if that's the case.
 
 - Check if crsr is the same as prev. 
    - If it is, set prev's next ptr to crsr.next.
 - Otherwise, set prev to prev.next
 - Move crsr ahead

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 