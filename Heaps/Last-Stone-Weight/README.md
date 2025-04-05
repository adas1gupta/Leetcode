# Leetcode 1046 - Last Stone Weight (Easy)

**Topic**: Heaps
**Link**: https://leetcode.com/problems/last-stone-weight/description/

## Notes: 
 - The problem asks you to take the two heaviest stones and smash them together where only the larger stone survives with a new value equal to the difference between the two stone weights. 
 - Keep going until you have one stone left. 
 - Turn all of the items in the list to its negative value and then heapify that new list.
 - The important thing to realize is that you want to stop when you only have one stone left, so that’s the while condition. 
    - Just keep smashing stones together until the length of the heap collection is equal to 1 or less than 1. 
 - Within the while loop:
    - Just pop the first, which is guaranteed to be the largest.
    - Pop the second, which is less than or equal to the first.
    - If first is greater than second, take their difference, invert it, and push it to the heap. 
 - Return 0 if the heap is empty or the negative of the top item in the heap. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(nlogn)
- Space: O(n)