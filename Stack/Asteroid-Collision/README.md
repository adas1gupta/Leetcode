# Leetcode 735 - Asteroid Collision (Medium)

**Topic**: Binary Search
**Link**: https://leetcode.com/problems/asteroid-collision/description/

## Notes: 
 - Utilize while else. 
 - Loop through the asteroids. 
 - While the top of the stack is a positive number and the asteroid you're on is a negative number, check if the asteroid has a larger absolute value. 
 - If it does, pop and continue. 
 - If it's equal, pop and break.
 - Otherwise, it means that the asteroid is a smaller value and we should move on to the next asteroid.
    - If that's the case, break out of the while loop.
 - In the else clause, simply append the asteroid. 


## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n) #n is the number of intervals
- Space: O(1) if result array is not counted as extra space. 