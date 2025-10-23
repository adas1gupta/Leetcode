# Leetcode 346 - Moving Average from Data Stream (Easy)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/moving-average-from-data-stream/description/

## Notes: 
 - This may be labelled a stack problem, but you should use a queue instead. 
 - Instead of recalculating total by summing the array, simply have a member variable that decrements whenever you remove from the queue and adds whenever you add something to the queue. 

 - Use a queue (deque) to maintain a sliding window of the last size elements, plus a running sum.
 - In next(val):
    - Add val to the queue and the running sum
    - If queue size exceeds size, remove the front element from both the queue and the sum
    - Return sum / queue.size()

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string