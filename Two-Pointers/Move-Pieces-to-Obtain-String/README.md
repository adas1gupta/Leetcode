# Leetcode 2337 - Move Pieces to Obtain a String (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/

## Notes: 
 - The key realization is that the first letter you encounter in start and target must match. 
 - For example, given this: _ _ _ _ L _ _ and _ _ _ R _ _ _:
 - If you encounter only one letter, then it's impossible for differentiating letters to create a match. 
 - Given this: _ _ _ _ _ L _ _ R _ and _ _ _ R _ _ L _
 - You'll reach L first for start and R for target, but R cannot swap over L, so they end up having to match. 
 - After you get a matching letter is when you check if the start's left is to the left of the target's left or if the start's right is to the right of target's right. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string