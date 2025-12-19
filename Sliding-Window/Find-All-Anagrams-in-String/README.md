# Leetcode 438 - Find All Anagrams in a String (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

## Notes: 
 - Very similar to the Minimum Window Substring problem.
 - Check for the obvious case of false where the second string is smaller than the first string. 
 - Afterwards, use the number of matches algorithm. 
 - Store the frequency of characters of the first string, initialize your window and second string dictionary, and keep track of the number of matches you need. 
 - In the first pass of the second string, track the frequency of characters within the length of the first string. 
 - Check if the current window is valid, and if it is, then append the left pointer to the list. 
 - Then, in the second pass, increment right and right's character count and increment left and decrement left's character count. 
 - Then, check if updating the right's character count creates more matches. 
 - IMPORTANT: do not check if updating left's character count creates more matches because you're updating left to point to a character that was already accounted for in the window. 
 - Once all that is done is when you return the list. 

## Mistakes:
 - Check left character is equal in both p and s_subset because you don't want to repeatedly decrement current_matches with something that's already mismatched.
    - Then, put that before you decrement the left character's count.

 - Make sure to append left + 1 because you haven't incremented left yet.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string