# Leetcode 336 - Palindrome Pairs (Hard)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/palindrome-pairs/description/

## Notes: 
 - to generate combinations, use this code: 
    - from itertools import combinations
    - itertools.combinations(x, y)
    - it generates an iterator of tuples
    - it takes in an iterable and the length of the tuples you want to generate
    - the benefit of this is that it preserves the order of the iterable you give it
 - Just read through the problem. 
 - It requires sorting based on timestamp
 - It requires a set for the combinations you generate because a user for a pattern only counts once. 
 - It also wants the lexicographically smallest pattern if frequencies are equal. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)