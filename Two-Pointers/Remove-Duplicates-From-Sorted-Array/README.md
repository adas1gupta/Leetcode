# Leetcode 26 - Remove Duplicates from Sorted Array (Easy)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

## Notes: 
 - Don't be trapped by the notion of swapping. DO NOT FOCUS ON SWAPPING!
 - Simply replace by having a pointer to the most recent unique number, incrementing it to the next spot, and then replacing whatever is there with the end pointer. 
 - For [0, 0, 1, 2, 3], the start pointer will increment to index 1, then index 1 will contain 1, and then when it goes to 2, then start will go to index 2, and index 2 will be 2. 
 - For [0, 1, 2, 2, 2], the start pointer will increment to index 1, and index 1 will contain the same number (1), and then it'll go to index 2 and contain the same number (2). 
 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string