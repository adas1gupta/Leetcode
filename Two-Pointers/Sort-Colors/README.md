# Leetcode 75 - Sort Colors (Medium)

**Topic**: Two Pointers  
**Link**: https://leetcode.com/problems/sort-colors/description/

## Notes: 
 - Have a left pointer mark the region for where 0s should be.
 - Have a right pointer mark the region for where 2s should be. 
 - Use the middle pointer as a scanner to shift left elements left and right elements right.
 - The problem with using separate if statements instead of using if, elif, else is that you might reach a point where mid is >= right. 
 - This causes a problem because by the time you exceed right, you're supposed to stop processing, but with separate if statements, you keep processing. 

 - Remember to increment mid in the nums[mid] == 0 section. 
 - Think about it this way:
    - If you land on a 2 first, you swap with right. 
    - However, you don't know what right gave you. 
    - That's why you need to stay put. 

 - If you land on a 1 first, it could be entirely possible that there are no 0s. 
 - If you encounter a 0 later, you swap with left, and what does left swap back to you? 
 - A 1. Can it be a 0? Can it be a 2? No way it can be a 2. 
 - So it has to be either a 1 or a 0. 
 - Now if it swaps a 0 back, then you keep mid put and swap it with left again. 
 - This supports not incrementing mid. 
 
 - However, what happens when you land on a 0 first? 
 - You swap onto yourself.
 - Then, you increment left, and swap the 0 onto left. 
 - If you get a 1, then mid increments, and you're left with 1 being behind 0 instead of being ahead of it. 

 - Also can't start mid ahead of left because left itself needs to be validated. (l, m, r = 0, 1, len(nums) - 1)

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(k) - number of unique characters in a string