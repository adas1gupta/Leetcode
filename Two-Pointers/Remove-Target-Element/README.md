# Leetcode 27 - Remove Element (Easy)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/remove-element/description/

## Notes: 
 - Don't do a while loop approach. 
 - Be mindful of the test case where, after swapping, start is equal to target element. 
 - Simply swap the target element to the end, and only increment start if it's not equal to the target element.
 - Then, return start because it will end up after the index with the last non-target element, but you're supposed to return length for the assertion, so length = the index of the last non-target element + 1 = start.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string