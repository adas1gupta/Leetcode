# Leetcode 33 - Search in Rotated Sorted Array (Medium)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/search-insert-position/description/

## Notes: 
 - Check if we're in the left sorted array or the right sorted array.
    - Just use the condition nums[left] <= mid
 - The subtle part here is realizing that left could be 4 and mid could be 7 and target could be 1. 
 - However, just checking if target <= mid isn't enough. 
    - You need to check if it's less than 4 as well, and if it's not, then you must search the right part. 
 - Same thing for right half. 
 - If mid < target, that isn't enough to search right part. 
 - Left array could be 6, 7, 8 and 8 is greater than mid (let's say 4), but not checking if target <= would lead us to check the right half. 

 - Just reduce this down to check if you're in left sorted part or right sorted part and then figure out which half to search based on if target is within that half or not. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 