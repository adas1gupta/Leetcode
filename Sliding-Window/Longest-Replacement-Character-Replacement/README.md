# Leetcode 424 - Longest Repeating Character Replacement (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/longest-repeating-character-replacement/description/

## Notes: 
 - The algorithm is basically maintaining a window and checking if the window is valid. 
 - A window is valid if the window_size - max_freq is <= k. 
 - If it's not, simply check left <= right and if the window_size - max_freq is <= k. 
 - You can update the max_freq = max(freq_dict.values()), and it'll still be an O(n) solution because the freq_dict will contain 26 characters at most. 
 - However, you don't need to because if you decrease the max_freq (NOT EXACTLY SURE WHY YET)


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string