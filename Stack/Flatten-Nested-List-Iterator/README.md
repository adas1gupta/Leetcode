# Leetcode 341 - Flatten Nested List Iterator (Medium)

**Topic**: Stack
**Link**: https://leetcode.com/problems/flatten-nested-list-iterator/description/

## Notes: 
 - Don't try and break down the Nested List into an actual list. 
 - Don't try to continually reverse in the first try. 
 - Think about lazily processing. 
 - Look at this test case:
 - [-3, -4, [-5, [-6, -7]]]
 - The [::-1] turns this into [[-5, [-6, -7]], -4, -3]. Notice how the inner list isn't reversed.
 - Then, we approach the Nested List, and when we reverse it, we get it [[[-6, -7], -5]]. Notice the pattern of how, level by level, the list is eventually reversed to the order that we want it in. 
 - This is why we don't need to continually reverse in the first try. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string