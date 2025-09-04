# Leetcode 340 - Longest Substring with At Most K Distinct Characters (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

## Notes: 
 - It says "At most", so the check should not be if len(s_dict) == k.
 - deleting a bucket key using del dict[key] is O(1) in this context. 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string