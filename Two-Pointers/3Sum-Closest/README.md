# Leetcode 16 - 3Sum Closest (Medium)

**Topic**: Tree, BFS
**Link**: https://leetcode.com/problems/3sum-closest/description/

## Notes: 
 - Don't care about duplicates here
    - This is because if your j and k are 5 + 2 and the target is 9, you still want to keep 5 in case you get 5 + 4, which is 9.
    - It doesn't matter if we go above or below the target. We want the closest absolute value difference.  
 - Don't get mixed up with using abs value and mistaking that to mean if the difference is < the target, we need to find a smaller value. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) -> explore all the nodes. 
- Space: O(h) -> height of the tree is the amount of space stored for the call stack