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
    - The reason why you have dictionaries is to store the frequency a corresponding x or y has. 
    - What you do is go through the list of y coordinates associated with an x coordinate in the dictionary for the original class. 
    - This is so you can see which points in the y dictionary has (x, y + val). 
      - val is the difference between the input y coordinate and the y coordinates associated with self.horizontals[x]. 
      - For example, the input can be (3, 2), and self.horizontals can have the point (3, 7), so that means you can form squares with length 5. 
    - Collect those lengths (e.g. 5) and their frequencies. 
    - Afterwards, your dictionaries will contain the actual edge lengths instead of possible combinations. 
      - For example, if the edge length you retrieve from self.verticals[ycoor] - x is 2, you are only storing 2 and not -2. 
   ```python
      for edge in xcoors.keys():
         if edge in ycoors and (x + edge, y + edge) in self.points:
            count += ycoors[edge] * xcoors[edge] * self.points[(x + edge, y + edge)]
         if -edge in ycoors and (x + edge, y - edge) in self.points:
            count += ycoors[-edge] * xcoors[edge] * self.points[(x + edge, y - edge)]
   ```
    - The different combinations are (x + edge, y +/- edge) for positive edge lengths. 
      - Positive edge lengths lie on the right side of the input point. 
    - For negative edge lengths, it would be (x - abs(edge), y +/- abs(edge)).
      - Negative edge lengths lie on the left side of the input point. 
    - The above is quite elegant because it checks (x + 2, y + 2) and (x + 2, y - 2) for positive edge lengths. 
    - For negative edge lengths, it checks (x + (-3), y - (-3) = y + 3) and (x + (-3), y + (-3)).
    - These calculations add up if you visualize the square. 
    ![alt text](image.png)
    - You can adjust the solution to iterate through y and calculate appropriate coordinates for x values. 
 - Finally, go through one of the dictionaries and visualize what points you would need if the positive and negative version of the current key you're on exists in the dictionary. 
 
## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(n)
- Space: O(1)