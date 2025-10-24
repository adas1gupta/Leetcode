# Leetcode 33 - Search in Rotated Sorted Array (Medium)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/search-insert-position/description/

## Notes: 
 - [1, 0, 1, 1, 1] leads to a case where you need to check if left == mid == right because if right was 2, array would be [1, 0, 1, 1, 2] and unrotated would be [0, 1, 1, 2, 1], which isn't a valid array.
 - Only way that left can be unsorted is that right is also equal to left.

 - Same as Search Rotated Sorted Array 1 but duplicates change it by adding an edge case where left could be <= mid but the array between and including left and mid is not sorted. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 