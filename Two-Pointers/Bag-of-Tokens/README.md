# Leetcode 948 - Bag of Tokens (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/bag-of-tokens/description/

## Notes: 
 - This is a hard problem.
 - Key pieces of intuition are that:
    - You want to check if after depleting score by 1, there are more than 1 tokens available to take
        - This is done by checking if end - start > 1
    - You want to keep collecting as many tokens as possible, and if there's a 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string