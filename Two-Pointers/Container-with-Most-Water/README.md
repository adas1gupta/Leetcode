# Leetcode 11 - Container with Most Water (Medium)

**Topic**: Two Pointer  
**Link**: https://leetcode.com/problems/container-with-most-water/description/

## Notes: 
 - Use a two pointer approach where right is at the end. 
 - Calculate the max area, and if the height at the right pointer is bigger, increment left. 
    - If the height at left is bigger, decrement right. 
    - The reason why you do this is because the limiting factors here are the width and the heights. 
    - To maximize height, you must stay with the taller height. 
    - Width will decrease no matter what. 
    - The only way you have to increase the area is to find the tallest heights, so you stay on the taller height and hope that increment or decrementing the other pointer will lead to a taller height. 
 - Return the max area. 
 - Whenever I’m asked a question about minimization or maximization, my first question should always be “what are the limiting factors?”

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)