# Leetcode 205 - Isomorphic Strings (Easy)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/bulls-and-cows/

## Notes: 
 - First pass, go through to find the bulls (matching characters in the same position)
 - Second pass, go through to find the cows. 
    - The important distinction is to make sure you aren't counting extra cows by simply encountering one of the bull characters that happen to have extra copies left. 
    - The bull character was already counted as a bull, so it cannot be counted as a cow. 
    - As a result, add the guessChar != secretChar. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string