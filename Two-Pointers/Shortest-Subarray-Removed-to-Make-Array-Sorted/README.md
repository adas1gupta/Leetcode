# Leetcode 1574 - Shortest Subarray to be Removed to Make Array Sorted (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/

## Notes: 
 - The algorithm is basically just breaking down the array into three parts: the left sorted prefix, the middle unsorted subarray to be removed, and the right sorted prefix. 
 - Given that, start from the right and find the point where right is just ahead of the unsorted subarray in the middle. 
 - Then, we set the maximum possible result to be returned to be right or right + 1 based on how you designed the first while loop (start of the sorted portion on the right). 
    - This is because [10, 9, 8, 3, 4, 5] would yield a right index of 3, and 3 - 0 (left) would be 3, which is the length of the array to be removed (the entire left half). 
 - Then, simply make sure left doesn't reach that right index. 
    - One edge case to worry about is what you want to do if you want to eliminate the right half of the array. 
    - If that's the case, 
 - Also, make sure that left doesn't reach the unsorted middle portion of the array. 
 - Once you do that, simply check if the element you are on in the left portion is actually less than the element on the right portion, and if not, increment right accordingly until it is. 
 - As left increases, the window/result continues to shrink, so keep checking the result against current right/right + 1 - left calculations. 
 - If you end up shifting right, still check. 
 - What guards an invalid window from being checked is this: "simply check if the element you are on in the left portion is actually less than the element on the right portion, and if not, increment right accordingly until it is."
 ```python
 if left > 0 and arr[left] < arr[left - 1]:
    break
 ```
 - This was quite a hard problem tbh. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string