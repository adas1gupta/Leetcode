# Leetcode 69 - Sqrt (Easy)

**Topic**: Basic Recursion
**Link**: https://leetcode.com/problems/sqrtx/description/

## Notes:

# Recursion 
 - Just perform recursive binary search.  
    - This is because you have a search space problem here. You start with the smallest number and keep going up linearly until you reach a number, when squared, reaches or exceeds the target value. 
    - Since this is in order and is a search, use binary search. 
 - Create a helper function that takes in left and right. 
 - If left passes right, that's equivalent to the while condition. The while condition is while left <= right, so the base case to end the recursive calls would be if left > right. 
 - Calculate mid and check if mid * mid == x. 
 - If it's not, check if it's less than x, and if it is, return helper(mid + 1, right). 
 - This is because your search space belongs to the right of the value that doesn't reach the target value. The right might contain a value big enough to meet the target value. 
 - If it's greater than x, return helper(left, mid - 1). 
    - This is because your search space belongs to the left of the value that exceeded the target value. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(logn) -> binary search
- Space: O(logn) -> logn calls 