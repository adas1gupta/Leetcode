# Leetcode 108 - Convert Sorted Array to Binary Search Tree (Easy)

**Topic**: BFS
**Link**: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

## Notes:

# BFS
 - nums = [-10, -3, 0, 5, 9]
                    ↑
                   mid=2
 
 - The array evenly splits into elements that should be on the left and on the right of the middle element. 
 - When you go to the left ([-10, -3]), you'll grab -10. 
    - To the left will be nothing. 
        - This is reflected when you call left and left will exceed right, indicating that between left and right are absolutely no elements.
    - This causes the right subtree to be built, automatically ensuring that the elements will be put into the right order. 
        - To the right will be 3.

 - 

 
## 🧪 Code
See `solution.py`

## ✅ Time & Space

# Recursion
- Time: O(n) -> number of nodes. 
- Space: O(n) -> complete binary tree introduces worst case space complexity of a level to be n // 2. 