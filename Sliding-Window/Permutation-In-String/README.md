# Leetcode 567 - Permutation in String (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/permutation-in-string/description/

## Notes: 
 - Very similar to the Minimum Window Substring problem.
 - Check for the obvious case of false where the second string is smaller than the first string. 
 - Afterwards, use the number of matches algorithm. 
 - Store the frequency of characters of the first string, initialize your window and second string dictionary, and keep track of the number of matches you need. 
 - In the first pass of the second string, track the frequency of characters within the length of the first string. 
 - Then, in the second pass, first check if the current window is valid. 
 - If not, increment right and right's character count and increment left and decrement left's character count. 
 - Then, check if updating the right's character count creates more matches. 
 - IMPORTANT: do not check if updating left's character count creates more matches because you're updating left to point to a character that was already accounted for in the window. 
 - Then, there's a possibility that the last window length will yield the needed number of matches. 
    - That's when you check one last time if the number of matches have been reached outside of the second pass. 
 - Once all that is done is when you return False. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string