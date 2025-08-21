# Leetcode 556 - Next Greater Element III (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/next-greater-element-iii/description/

## Notes: 
 - Algorithm is always:
    - start from the back
    - Find the element where the element to the left is less than the element to the right
    - Record that element that is less than the element to the right.
    - Start from the back again and find the smallest element that is greater than the element to the left.
    - Record that element and then swap the two recorded elements. 
    - Then, from the element that was swapped to the left (smallest element greater than the left), but not including it: reverse from that element to the end. 
    - After you do that, there is an edge case where the number you form is greater than or equal to 2^32. If that's the case, return -1. 
 - Before you try to find the smallest element that is greater than the element to the left, check if there is an actual pivot, and if there isn't, return -1. 
 - Then, before you try to swap, check if there is a smallest element that is greater than the element to the left. If not, return -1. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string