# Leetcode 125 - Valid Palindrome (Easy)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/valid-palindrome/description/

## Notes: 
 - Just read the question.
 - Keep in mind that the input is not perfectly alphanumeric.
 - Also, numbers count, so look for alphanumeric instead of alphabetical 

 - When you use a while loop to skip past nonalphanumeric characters, make sure to check that left <= right before index access.
    - If not, just break.

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string