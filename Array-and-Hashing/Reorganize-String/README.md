# Leetcode 767 - Reorganize String (Medium)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/reorganize-string/description/

## Notes: 
 - You care about the most frequent and second most frequent character
 - Since you want to to map characters to frequencies and frequencies to characters, you can use a dictionary in conjunction with a heap or array buckets. 
 - Heap is used here because it's less complex to implement even though it can perform worse theoretically. 
 - The time complexity is n log k where k is the number of unique characters. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n log k)
- Space: O(1)