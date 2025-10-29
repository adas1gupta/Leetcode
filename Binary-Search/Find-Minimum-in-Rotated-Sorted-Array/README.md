# Leetcode 153 - Find Minimum in Rotated Sorted Array (Medium)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

## Notes: 
 - Check to see if mid > right. 
 - If it is, that means the minimum has to be to the right half. 
    - Remember that the mid calculation always rounds down (0 + 1 = 0)
    - Also, remember that the mid we are on might be the minimum, so we set right = to it. 
 - Since minimum is right half, we set left = mid + 1
 
 - Since mid could be the minimum, we set right = mid. 
 - However, near the end, left will equal to right and that will equal the minimum. 
    - That's why the while loop needs to change from left <= right to left < right. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 