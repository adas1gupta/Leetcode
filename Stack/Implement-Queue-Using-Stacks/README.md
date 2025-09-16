# Leetcode 232 - Implement Queue using Stacks (Easy)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/implement-queue-using-stacks/description/

## Notes: 
 - A pretty interesting observation can be used here to help solve this problem efficiently. 
 - Append 1, 2, and 3 ([1, 2, 3, 4]). 
 - You want to pop the 1, so one approach you can do is using two stacks to hold the pops from the first stack so you can pop the last item. 
 - Second will be [4, 3, 2] and first will be [1]. What's interesting is that the next element you would want to pop is 2, and it's conveniently the last item in the second stack. 
 - This changes peek as well because that means you first want to check if the second stack is empty before checking the first element in the first stack.
    - This is because of test cases where you pop, then continually push, then want to peek/pop again. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string