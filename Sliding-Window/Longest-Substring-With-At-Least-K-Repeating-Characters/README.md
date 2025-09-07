# Leetcode 395 - Longest Substring with At Least K Repeating Characters (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

## Notes: 
 - This utilizes the number of matches algorithm, but in a different way. 
 - This is because you don't know the number of matches you're actually looking for. 
    - There can be 10 unique characters with at least K frequency or 4. 
 - This is why you have to loop through the possibility of unique characters (for i in range(1, 27)). 
 - After you do, you simply keep a tracker for the number of characters you see with at least K frequency and the number of unique characters you see. 
 - Initialize the window, and then check if the character you're on is unique. 
    - If it is, increment the unique characters tracker. 
 - Then, increment the frequency of the character you're on and see if it matches K. 
    - If it does, then increment the number of characters you see with at least K frequency tracker. 
 - Afterwards, this is where you check if you have to increment the left pointer. 
    - You increment left if the unique characters tracker exceeds the current number of matches you're looking for. 
    - Make sure to decrement both trackers in their appropriate scenarios. 
 - Then, adjust the longest substring you've found if the number of characters you see with at least k frequency matches the number of unique characters you see and if the number of unique characters equal the current number of matches you're looking for. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string