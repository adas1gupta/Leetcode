# Leetcode 387 - First unique character in a string (Easy)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/first-unique-character-in-a-string/

## Notes: 
 - hashmap to store the frequencies.
 - The frequencies are used because the pattern is that characters that occur an even number of times is completely used. 
 - The characters that occur an odd number of times is used except for 1. 
 - One character can be part of the middle, so add a boolean check to see if you ever encounter a single odd frequency. 
 - Once frequency collection is done, implement the pattern. 
 - There's an important distinction that needs to be made with this problem. 
    - The space complexity is O(1) and not O(n) even though a hashmap is involved. 
 - There's also another alternative where you use an array to store 52 characters. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)