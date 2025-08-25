# Leetcode 3 - Longest Substring Without Repeating Characters (Medium)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

## Notes: 
 - Use a dictionary to keep track of frequencies
 - If frequency of the current character is 0, then calculate the maximum. 
 - Otherwise, use a while loop to update the anchor until it finally reaches a point where the character that the scanner is on is not present. 
    - The key part here is that you need to use a while loop because anchor might not be on the duplicate character. 
    - You also need to update the frequency of the character after you check and not in the if or else part of the code. 
 - Finally, return the maximum. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string