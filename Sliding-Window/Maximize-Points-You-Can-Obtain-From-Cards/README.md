# Leetcode 1423 - Maximum Points You Can Obtain from Cards (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

## Notes: 
 - The combinations that you can get are k elements from the right, 0 from left, k - 1 from right, 1 from left, k - 2 from right, 3 from left. 
 - Basically, you're starting k elements from the right and then subtracting as you increment right pointer forward.
 - Then, you increment left pointer forward simultaneously and add elements from the right. 
 - Start with initializing the sum as the sum of the elements from the right. 
 - Then, loop through k and subtract from right and add from left. 
 - Compare the max_sum between what you have recorded and what you've found. 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string