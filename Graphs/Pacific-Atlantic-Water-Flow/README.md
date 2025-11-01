# Leetcode 417 - Pacific Atlantic Water Flow (Medium)

**Topic**: Graphs, DFS 
**Link**: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

## Notes: 
 - Start from the ends with Pacific ocean and Atlantic ocean. 
 - Have a pacific set and an atlantic set.

 - This is hard in terms of implementing, not conceptually. 
 
 - dfs is straight forward.
 - You need the previous height to make a comparison for the base case. Just use previous height instead of previous coordinates.
 - *However, you should also pass in the atlantic/pacific set so you know which set to add to.*
 
 - Then, go through ROWS. Don't do a nested for loop. Just calculate what values yield pacific and atlantic. 
 - Then, go through COLS. 
 - Then, build the result list. 

## 🧪 Code
See `solution.py`

## ✅ Time & Space
- Time: O(V + E) where V is number of vertices and E is number of edges
- Space: O(V)