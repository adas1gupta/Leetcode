# Leetcode 138 - Copy List with Random Pointer (Medium)

**Topic**: Intervals
**Link**: https://leetcode.com/problems/copy-list-with-random-pointer/description/

## Notes: 
 - It's obvious you need to use a hashmap for this problem.

 - You can do this problem in 2 passes. 
 - First pass, just make a copy of the nodes and don't worry about adjusting the next or random pointers yet.
 - Just be mindful that nodes can point to None, and you won't be storing None in the dictionary because the while loop stops before the None

 - Second pass, adjust the pointers using the hashmap and make sure to handle the None case


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 