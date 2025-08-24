# Leetcode 31 - Next Permutation (Medium)

**Topic**: Two Pointers 
**Link**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Notes: 
 - The algorithm is finding the element that is < the element after it, starting from the back.
 - Then, starting from the back, find the smallest element greater than the pattern breaking element.
 - Swap them, and from the element after the pattern breaking element index, reverse the order of the elements. 
 - When you perform the swap, it's guaranteed to be in non-increasing order. 
 - You reverse the rest of the array instead of the elements between the swapped indices because reversing non-increasing means you'll get an increasing order, which is lexicographically the smallest. 
    - [5, 4, 3, 2, 1] becoming [1, 2, 3, 4, 5] is lexicographically the smallest available permutation left. 
 - You're performing the swap with the next smallest number that is > the pivot element because that is the next lexicographically available starting option. 
 - Be careful of the edge case where the entire array is non-increasing. If that's the case, then check, don't swap, and reverse as normal. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string