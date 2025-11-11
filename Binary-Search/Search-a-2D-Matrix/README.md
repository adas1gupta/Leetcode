# Leetcode 74 - Search a 2D Matrix (Medium)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/search-a-2d-matrix/description/

## Notes: 
 - Outer binary, inner binary. Pretty straightfoward. 

 - Need to remember that after evaluating that the target is within a certain row, it can't be in other rows, so immediately return False
    - Just gotta reason through it end to end. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 