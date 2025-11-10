# Leetcode 238 - Product of Array Except Self (Medium)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/product-of-array-except-self/description/

## Notes: 
 - For each value in the array, the (formula is everything to the left to the value multipled) multipled with (everything to the right of the value multiplied).

 - Since you want stuff to the left, you store what was accumulated from the left. 
 - Then you modify left, so that left is whatever is accumulated before the current item you're on. 

 - Same logic for right. 
 - What's accumulated before the last item is 1, so you multiply the last item with 1 to keep the value the same. 
 - Then, you accumulate the right, multiply by the accumulated right, and then update right.

        
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)