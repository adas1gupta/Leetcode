# Leetcode 76 - Minimum Window Substring (Hard)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/longest-repeating-character-replacement/description/

## Notes: 
 - Collect the frequencies of characters in string T. 
 - Have a container for the frequencies of characters in string S. 
 - Have pointers established for the window.
 - Have pointers established to mark the window that you see with the smallest size and fulfilling the conditions. 
 - Have a variable to track the smallest substring length that you've seen so far. 
 - Now, the key here is to track the current number of matches you have and the number of matches you need to have. 
 - Then, in the while loop, collect the frequency of each character you go through in string S. 
 - The important thing here is that when you're checking for matches, you check if the frequency is equal to the frequency in string T, not >=. 
    - This is because it'll match the frequency once it's equal, and afterwards, you'll keep increasing matches even though you're not getting more matches. 
 - If you do end up achieving the needed amount of matches, use a while loop to measure the window as you continually decrease the window from the left and subtract the frequency

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string