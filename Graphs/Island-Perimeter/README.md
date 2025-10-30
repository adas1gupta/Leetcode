# Leetcode 463 - Island Perimeter (Easy)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/island-perimeter/description/

## Notes: 
 - Visited set to store coordinates visited 
 
 - Make a inner dfs function
    - Base cases of out of bounds, coordinate being water (0), or coordinate being in visited
    - Add the coordinate to the visited set. 
    - Set perimeter equal to one of the dfs calls to either, (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
 
    - Then, after calling to one of them, it'll continue onto that side until it reaches a base case. 
    - Then, it'll pop back and go to the most recent 1 visited, and then go to the next direction. 
    - Perimeter will have a value, so you need to += for the rest of the directions. 
 
 - We need to return perimeter because perimeter accumulates and perimeter (the value we're collecting) is = dfs(one of the four directions)

 - In the outer function, loop through the array and call dfs on an island (1).

 - This is O(m * n) time complexity because we will find the first instance of land and then compute the entire island.
    - This part is O(land cells). 
 - After every single instance of land, we'll immediately reach base cases, and the base cases will return 0 since they're visited. 
    - This is O(1) complexity for visited islands. 
 - Since we're going through every item in the 2D array, that's O(m * n)

 - O(m * n) space complexity because visited can store all the cells if all cells are land cells. 
 - Call stack is O(land cells), which is O(m * n). 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)