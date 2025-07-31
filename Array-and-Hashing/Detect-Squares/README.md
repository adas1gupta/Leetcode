# Leetcode 2013. Detect Squares (Medium)

**Topic**: Arrays & Hashing  
**Link**: https://leetcode.com/problems/detect-squares/description/

## Notes: 
 - Keep in mind that (x + 0, y + 0) isn't a valid square because the square becomes one point. 
 - Store the x coordinates along with points that share that x coordinate.
 - Store the y coordinates along with points that share that y coordinate. 
 - Store the frequency of each point. 
    - This is because the formula to calculate number of ways is frequency of each point multiplied together because each point is treated as a separate point. 
 - Afterwards, given a point, first check if its coordinates are actually in the x coordinate or y coordinate dictionaries. 
    - Don't check if the point is in the self.points dictionary because it's entirely possible that the point is brand new, but you can form multiple squares with it. 
 - Then, store the edge lengths that you can make by going through the x coordinates dictionary and y coordinates dictionary. 
    - Make sure to avoid the case mentioned in the first bullet point with edge lengths of 0. 
 - Finally, go through one of the dictionaries and visualize what points you would need if the positive and negative version of the current key you're on exists in the dictionary. 
 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)