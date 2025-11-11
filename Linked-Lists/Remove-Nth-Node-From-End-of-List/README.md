# Leetcode 19 - Remove Nth Node From End of List (Medium)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

## Notes: 
 - This is very similar to fast and slow, but it's more similar to sliding window.

 - Idea is that you have a window between slow and fast that is of size n + 1. 
 - This is because when fast reaches the end, you'll be at the node behind the nth node because of the size of window. 
 
 - Start from a dummy node.
    - The reason why you do this is because the head might be the node you want to remove.
    - In that case, fast will automatically reach the end, so slow will be equal to the dummy node. 
 
 - Then, just set slow.next = dummy.next.next
 - Start both slow and fast from the dummy node. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 