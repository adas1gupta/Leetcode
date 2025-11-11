# Leetcode 704 - Binary Search (Easy)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/binary-search/description/

## Notes: 
 - Just remember to keep left <= right. 
 - Think about the test case [1, 3, 5] and your target is 5. 
    - You'll look at 3, then move left to 3, then look at 3 again and move left to 5. 
    - Left will be equal to 5 but you haven't checked 5 because left < right.


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 