# Leetcode 977 - Squares of a Sorted Array (Easy)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/squares-of-a-sorted-array/description/

## Notes: 
 - The key piece of intuition is that you compare the end and the beginning for the largest element, and once you do, you'll have an array of elements from largest to smallest. 
 - Simply reverse that array and return it. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string