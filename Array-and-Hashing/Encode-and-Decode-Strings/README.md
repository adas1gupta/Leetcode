# Leetcode 271 - Encode and Decode Strings (Medium)

**Topic**: Arrays & Hashing  
**Link**: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

## Notes: 
 - When you start looping through the string in decode, use two pointers. 
 - Have i mark the beginning of an integer, and have j go until YOU REACH A "#". 
 - Once you do, append input_str[j + 1: j + 1 + int(input_str[i:j])].

 - In your decode, aim to complete the following three tasks each iteration of the while loop. 
    - Grab the number because you're guaranteed to start on a number before the #. 
    - Grab the word using the length and starting after the #.
    - Change start to the new position to collect the next number. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(n)